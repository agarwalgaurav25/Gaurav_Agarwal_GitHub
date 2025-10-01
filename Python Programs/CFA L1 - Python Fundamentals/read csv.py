import pandas as pd
pd.set_option('display.max_columns',None)


P_df = pd.read_csv('investors_data.csv')
P_df.info()
P_df.isnull()
p_mean = P_df["Portfolio Size"].mean()
median_period = P_df["Years with Investment Firm"].median()
P_df['Portfolio Size'].fillna(p_mean,inplace = True)
P_df['Years with Investment Firm'].fillna(median_period,inplace = True)
print(P_df)
# print ("hi" + P_df["First Name"]+P_df["Last Name"] + "ho you doin")