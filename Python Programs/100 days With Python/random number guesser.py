import random as rd
com_num = rd.randint(1,10)
print(com_num)
user_num = 0
while user_num != com_num:
    user_num =int(input("enter the number you think the game will produce "))
    if user_num == com_num:
            print ('you guessed it right')
    else:
            while user_num != com_num:
                if user_num > com_num:
                    print ("try again")
                    print("too high")
                elif user_num < com_num:
                    print("too low")
                    print ("try again")
                
                break
    