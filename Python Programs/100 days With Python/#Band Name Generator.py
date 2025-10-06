print('''Welcome to the Band Name Generator''')
city_name = str(input("What's the name of your city ? \n"))
pet_name = str(input("What's the name of your pet ? \n"))
band_name = city_name + " " + pet_name

username = input("enter your name ")
age = int(input('enter your age \n'))
Class_ = str(input('enter your class\n'))
f_name = input("enter your father's name\n")
print("Name : ", username,
"\n Age :", age,
"\n Father's Name :", f_name,
"\n Class : ", Class_)


stocks_names = ['Apple', 'Samsung', 'Alibaba', 'Novo Nordisk', 'Naspers']
stock_prices = [142, 45, 12, 125, 30]

for c in range(4,0,-1):
    # in reverse hence -1 step
    a = stock_prices[c]
    b = stocks_names[c]
    print (' the price of ', stocks_names[c])

