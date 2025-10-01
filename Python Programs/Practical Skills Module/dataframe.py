import pandas as pd
portfolio_df= pd.DataFrame({"Stock Name":["Apple","Google","PayPal"],
"Price":[200,100,300],"EPS":[10,20,15]})
print(portfolio_df.describe())
print(portfolio_df.head(2))
print(sum(portfolio_df['Price']))
no_of_companies = len(portfolio_df["Stock Name"])
print((sum(portfolio_df["EPS"]))/no_of_companies)
print(portfolio_df.tail(2))
portfolio_df.info()
print(portfolio_df["EPS"].median())