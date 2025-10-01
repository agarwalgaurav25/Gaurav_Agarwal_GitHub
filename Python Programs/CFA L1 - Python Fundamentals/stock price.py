stock = {"infosys": 1525 , "HDFC": 960, "Zomato":321}
avg = ((stock["infosys"] + stock['HDFC'] + stock['Zomato'])/len(stock))
print (avg)
stock ["Tata"] = 400
del stock["infosys"]
print (stock)
print (stock.values())
print ((sum(stock.values())/len(stock)))

a = 0
snum = 0
while a < 5:
	snum= snum  +a
	a += 1
print (snum)

feedback = str(input('''enter your feedback
	'''))
print(feedback.split('.'))
email = str(input('enter email \n'))
list = email.split('.')
print(list[0])


revenue_A = 2500
revenue_B = 2000
print(revenue_A == revenue_B)
print(revenue_A != revenue_B)
print(revenue_A > revenue_B)
print(revenue_A < revenue_B)

