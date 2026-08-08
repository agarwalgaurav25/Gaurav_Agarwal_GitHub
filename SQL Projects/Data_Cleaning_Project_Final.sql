/* ============================================================
   PROJECT: Layoffs Dataset — SQL Data Cleaning
   ------------------------------------------------------------
   Goal: Clean a raw "layoffs" dataset in MySQL by:
     1. Removing duplicate records
     2. Standardising inconsistent data
     3. Handling NULL / blank values
     4. Removing unnecessary columns

   Guiding principle: never alter the raw table directly.
   All work is done on staging copies so the original data
   remains untouched and recoverable at any point.
   ============================================================ */


-- ------------------------------------------------------------
-- 0. Inspect the raw data
-- ------------------------------------------------------------
SELECT *
FROM layoffs;


-- ------------------------------------------------------------
-- STEP 1: Remove Duplicates
-- ------------------------------------------------------------

-- 1.1 Create a staging table with the same structure as the
--     raw table (no data copied yet). All cleaning happens here.
CREATE TABLE IF NOT EXISTS layoffs_staging
LIKE layoffs;

-- Sanity check: staging should be empty at this point
SELECT *
FROM layoffs_staging;

-- 1.2 Copy all raw data into the staging table
INSERT layoffs_staging
SELECT *
FROM layoffs;


-- 1.3 First attempt at flagging duplicates.
--     ROW_NUMBER() is used with a PARTITION BY clause on a set
--     of columns that, together, are assumed to make a row
--     unique. Within each partition, the first occurrence gets
--     row_num = 1, the second gets row_num = 2, and so on —
--     so anything with row_num > 1 is a duplicate.
SELECT *,
       ROW_NUMBER() OVER (
           PARTITION BY company, industry, total_laid_off,
                        percentage_laid_off, `date`
       ) AS row_num
FROM layoffs_staging;

-- Wrap the above in a CTE so we can filter directly on row_num
WITH duplicates_cte AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY company, industry, total_laid_off,
                            percentage_laid_off, `date`
           ) AS row_num
    FROM layoffs_staging
)
SELECT *
FROM duplicates_cte
WHERE row_num > 1;

-- 1.4 Validate the assumption: does this column combination
--     actually guarantee uniqueness?
SELECT *
FROM layoffs_staging
WHERE company IN ('Casper', 'Cazoo', 'Hibob', 'Oda');

-- Finding: 'Oda' operates in multiple countries, but `country`
-- wasn't part of the PARTITION BY — so genuinely different rows
-- (same company, different country) were being flagged as
-- duplicates. The original column set wasn't strict enough.

-- 1.5 Fix: partition by ALL columns, so only rows that are
--     identical across every field are marked as duplicates.
WITH duplicates_updated_cte AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY company, location, industry, total_laid_off,
                            `date`, stage, country, funds_raised_millions
           ) AS row_num
    FROM layoffs_staging
)
SELECT *
FROM duplicates_updated_cte
WHERE row_num > 1;

-- Note: MySQL does not allow DELETE or UPDATE directly on a CTE,
-- so duplicates can't be removed from this query alone.

-- 1.6 Workaround: create a second staging table identical to
--     layoffs_staging, plus an extra row_num column. This can be
--     generated via: right-click layoffs_staging → Copy to
--     Clipboard → "Create Statement", then add the row_num column.
CREATE TABLE `layoffs_staging2` (
  `company` text,
  `location` text,
  `industry` text,
  `total_laid_off` bigint DEFAULT NULL,
  `percentage_laid_off` text,
  `date` text,
  `stage` text,
  `country` text,
  `funds_raised_millions` int DEFAULT NULL,
  `row_num` int
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/* Two ways to populate layoffs_staging2 from here:
     a) INSERT using the CTE, filtering WHERE row_num = 1
        directly (keeps only first occurrences), OR
     b) INSERT all rows including row_num, then SELECT
        WHERE row_num > 1 to confirm the duplicates, and
        finally DELETE those rows.
   Option (b) is used below, since it's easier to audit
   before deleting anything. */

INSERT INTO layoffs_staging2
SELECT *,
       ROW_NUMBER() OVER (
           PARTITION BY company, location, industry, total_laid_off,
                        `date`, stage, country, funds_raised_millions
       ) AS row_num
FROM layoffs_staging;

-- Confirm all rows landed correctly
SELECT *
FROM layoffs_staging2;

-- Review duplicates before deleting (good practice: check before you delete)
SELECT *
FROM layoffs_staging2
WHERE row_num > 1;

-- Remove the confirmed duplicates
DELETE
FROM layoffs_staging2
WHERE row_num > 1;


-- ------------------------------------------------------------
-- STEP 2: Standardise the Data
-- ------------------------------------------------------------

-- 2.1 Company names: strip leading/trailing whitespace
SELECT company, TRIM(company)
FROM layoffs_staging2;

UPDATE layoffs_staging2
SET company = TRIM(company);

-- 2.2 Scan each categorical column with DISTINCT to spot
--     inconsistent/near-duplicate values
SELECT DISTINCT industry
FROM layoffs_staging2
ORDER BY 1 ASC;

SELECT DISTINCT location
FROM layoffs_staging2
ORDER BY 1 ASC;

SELECT DISTINCT country
FROM layoffs_staging2
ORDER BY 1 ASC;

-- Finding: "United States" appears with a trailing "." on some
-- rows, effectively creating a duplicate category. Standardise
-- everything to a single value.
UPDATE layoffs_staging2
SET country = 'USA'
WHERE country LIKE '%United States%';

-- Finding: "Crypto" appears under 3 slightly different spellings/
-- casings. Inspect, then standardise to one canonical value.
SELECT *
FROM layoffs_staging2
WHERE industry LIKE '%crypto%';

UPDATE layoffs_staging2
SET industry = 'Crypto'
WHERE industry LIKE '%crypto%';

-- 2.3 Convert `date` from text to a proper DATE type, since
--     later analysis will involve time-series work.
SELECT `date`
FROM layoffs_staging2;

-- Note: STR_TO_DATE is case-sensitive on its format tokens —
-- lowercase 'y' parses incorrectly; uppercase 'Y' is required
-- for a 4-digit year. (Worth checking the MySQL date-format
-- reference for the full token list.)
SELECT `date`, STR_TO_DATE(`date`, '%m/%d/%y')  -- incorrect: lowercase Y
FROM layoffs_staging2;

SELECT `date`, STR_TO_DATE(`date`, '%m/%d/%Y')  -- correct
FROM layoffs_staging2;

-- Apply the reformat first — this keeps the column as text but
-- in proper date format, which is required before ALTER can
-- convert the column type without erroring out.
UPDATE layoffs_staging2
SET `date` = STR_TO_DATE(`date`, '%m/%d/%Y');

ALTER TABLE layoffs_staging2
MODIFY COLUMN `date` DATE;


-- ------------------------------------------------------------
-- STEP 3: Handle NULL / Blank Values
-- ------------------------------------------------------------

-- 3.1 Normalise blanks to proper NULLs so they can be handled
--     consistently (blank strings and NULL are not the same
--     thing in SQL, and blanks are easy to miss otherwise).
UPDATE layoffs_staging2
SET industry = NULL
WHERE industry = '';

-- 3.2 Self-join on company name to find cases where the same
--     company has `industry` populated in some rows but NULL in
--     others — these can be backfilled from the known value.
SELECT t1.industry, t2.industry
FROM layoffs_staging2 t1
JOIN layoffs_staging2 t2
    ON t1.company = t2.company
WHERE t1.industry IS NULL
  AND t2.industry IS NOT NULL;

-- 3.3 Apply the backfill
UPDATE layoffs_staging2 t1
JOIN layoffs_staging2 t2
    ON t1.company = t2.company
SET t1.industry = t2.industry
WHERE t1.industry IS NULL
  AND t2.industry IS NOT NULL;

-- Check what's left — any remaining NULLs have no matching
-- non-null record for that company anywhere in the table, so
-- they can't be inferred and are left as genuine NULLs.
SELECT company, industry
FROM layoffs_staging2
WHERE industry IS NULL;


-- ------------------------------------------------------------
-- STEP 4: Remove Unnecessary Columns
-- ------------------------------------------------------------

-- row_num was only ever a helper column for de-duplication —
-- drop it now that cleaning is complete. This is safe because
-- it only affects layoffs_staging2, never the raw `layoffs` table.
ALTER TABLE layoffs_staging2
DROP COLUMN row_num;


-- ------------------------------------------------------------
-- Final cleaned dataset
-- ------------------------------------------------------------
SELECT *
FROM layoffs_staging2;
