"""Small utility to compute the median of a list of numbers.

Usage examples:
    >>> median([3, 1, 4])
    3
    >>> median([3, 1, 4, 2])
    2.5

Run from CLI:
    python "Python Programs/find_median.py" 3 1 4 2
    python "Python Programs/find_median.py" "[3,1,4,2]"
    echo "3 1 4 2" | python "Python Programs/find_median.py"
"""
from typing import Iterable, List, Sequence


def median(data: Iterable[float]) -> float:
    """Return the median of the provided iterable of numbers.

    Raises ValueError for empty input.
    """
    # Convert to list so we can index and sort without mutating caller data
    values: List[float] = list(data)
    if len(values) == 0:
        raise ValueError("median requires at least one data point")
    values.sort()
    n = len(values)
    mid = n // 2
    if n % 2 == 1:
        return float(values[mid])
    else:
        return (values[mid - 1] + values[mid]) / 2.0


if __name__ == '__main__':
    import sys
    import ast

    def parse_args(argv: Sequence[str]) -> List[float]:
        # If arguments are provided, attempt to parse a Python-style list or individual numbers
        if len(argv) >= 2:
            text = ' '.join(argv[1:]).strip()
            # Try literal eval first (handles: "[1,2,3]" or "(1,2,3)")
            try:
                obj = ast.literal_eval(text)
                if isinstance(obj, (int, float)):
                    return [float(obj)]
                elif isinstance(obj, (list, tuple)):
                    return [float(x) for x in obj]
            except Exception:
                pass
            # Fall back to splitting on whitespace or commas
            parts = text.replace(',', ' ').split()
            return [float(x) for x in parts]
        # No args -> try reading a line from stdin or interactive input
        try:
            s = sys.stdin.read().strip()
        except Exception:
            s = ''
        if s:
            parts = s.replace(',', ' ').split()
            return [float(x) for x in parts]
        # If still empty, prompt user
        s = input('Enter numbers separated by spaces: ')
        return [float(x) for x in s.replace(',', ' ').split()]

    try:
        nums = parse_args(sys.argv)
        result = median(nums)
        print(result)
    except ValueError as ve:
        print('Error:', ve)
        sys.exit(1)
    except Exception as e:
        print('Could not parse input or compute median:', e)
        sys.exit(2)
