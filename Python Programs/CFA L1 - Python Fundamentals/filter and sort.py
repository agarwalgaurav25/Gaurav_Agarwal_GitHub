import pandas as pd
investors_df = pd.read_csv('investors_data.csv')
print(investors_df)
investors_df.describe()
print(investors_df.info())
# loyal_df = (investors_df[investors_df["Years with Investment Firm"] >= 15])

# name_df = investors_df.sort_values(by = "First Name")
# print (name_df)
investors_df['Portfolio Size'].fillna(investors_df['Portfolio Size'].mean(), inplace = True )
print(investors_df)