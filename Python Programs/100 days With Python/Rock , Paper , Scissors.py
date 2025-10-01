import random as rd
print ( "Welcome to to rock , papers and Scissors")
# name = str(input("enter you name: "))
# print (" 0 = Rock , 1 = scissors , 2 = papers")
# comp = rd.randint(0,2)
# user = int(input("enter your response ").strip())

# if user == 1 :
#     print()

comp = rd.randint(1,2)
if comp == 1 :
    print ( "heads")
elif comp == 2 :
    print ('tails')