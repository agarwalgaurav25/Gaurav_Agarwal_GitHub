div = int(input("Enter this year’s dividend: "))
div_g= float(input("Enter the company’s expected dividend growth: "))
Ke = float(input("Enter the company’s cost of equity: "))
price = float(input("Enter the current stock price: "))

ddm = ((div/ ((Ke - div_g ))))
if  ddm > price:
    print ("The stock is undervalued @", price)
elif ddm < price:
    print ("The stock is overvalued @ ", price)
elif ddm == price  :
    print ("The stock is correctly valued @ ", price)