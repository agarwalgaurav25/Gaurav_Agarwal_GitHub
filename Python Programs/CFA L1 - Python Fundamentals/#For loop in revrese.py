stocks_names = ['Apple', 'Samsung', 'Alibaba', 'Novo Nordisk', 'Naspers']
stock_prices = [142, 45, 12, 125, 30]
print ('in reverse order')
for i in range(4,-1,-1):
    # in reverse hence -1 step
    print ('index = ', i)
    print (f'The price of {stocks_names[i]} is ${stock_prices[i]}')

print (' in reverse but in even positions ')
for i in range(4,-1,-2):
    # in reverse hence -1 step
    print ('index = ', i)
    print (f'The price of {stocks_names[i]} is ${stock_prices[i]}')
a = 4   
while a >= 0:
    print ("index = ", a)
    print(f'The price of {stocks_names[a]}is {stock_prices[a]}')
    a = a - 1