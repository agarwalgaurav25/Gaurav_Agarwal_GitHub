num = (input("enter the number upto which u wanna find if perfect square or not : "))
num_list = num.split(",")
print(num_list)
print(type(num_list))
print(num_list)
sq_list = []
for i in num_list:
    i = float(i)
    if ( ((i**0.5)-int(i**0.5)) == 0 ):
        print(f'{i} is a perfect Square')
        sq_list.append(i)
    else:
        print(f'{i} is a not perfect Square')
print (sq_list)