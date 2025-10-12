import random 
from prettytable import PrettyTable
from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("CadetBlue")
# timmy.fd(100)
# timmy.color("coral")
# timmy.fd(100)
# print (timmy)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

table = PrettyTable()

table.add_column("Pokemon", ["Squirtle","Pikachu", "Charmander", "Bulbasaur"],"c")
table.add_column("Type",["Water","Electric","Fire","forest"],"r")
print(table)

# # print ("Program to get heads and tails")
# # a = rd.randint(0,1)
# # if a == 1 :
# # 	print ("Heads")
# # else:
# # # 	print ("Tails")

# # print("program to fund who pays the bill")
# # friends = ["nilay","Gaurav","Dhruv","Garv"]
# # last_index = (len(friends) - 1 )
# # a = rd.randint(0,last_index)
# # print (f'The person to pay the bill is {friends[a]}')
# # person = rd.choice(friends)
# # print (person)
# # print (f'the person to pay the bill is {rd.choice(friends)}')

# # fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# # vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# # dirty_dozen = [fruits, vegetables]
 
# # print(dirty_dozen[1][1])

# # # Then print out:

# # print(dirty_dozen[0])
# # print(dirty_dozen[1])
# # # To see what happens at the next stage print out:

# # print(dirty_dozen[1][2])
# # print(dirty_dozen[1][3])


# pictures = ["""

#     _       ,/'
#    (_).  ,/'
#    __  ::
#   (__)'  `/.
#             `/.
# """

# , """
#       ,--.--._
# ------" _, ___)
#         / _/____)
#           /(____)
# ------      (__)
#        `-----"
#  """

# ,'''
#             ___..__
#   __..--""" ._ __.'
#               "-..__
#             '"--..__";
#  ___        '--...__"";
#     `-..__ '"---..._;"
#           ----'      
# ''']
# user = int(input("Enter 0 for rock ,  1 for paper , 2 for scissors \n"))
# comp = random.randint(0,2)
# print (f''' user chose 
# 	{pictures[user]}''')
# print ( f''' comp chose 
# 	{pictures[comp]}''')





# if comp == user:
# 	print ("its a tie")
# else:
# 	if comp == 1:
# 		if user == 0:
# 			print ("You Lose")
# 		elif user == 2:
# 			print("You win")
# 	if comp == 2 :
# 		if user == 0:
# 			print ("you win")
# 		elif user == 1 :
# 			print ("you lose")
# 	if comp == 0 :
# 		if user == 1:
# 			print ("you win")
# 		elif user == 2 :
# 			print ("you lose")


# b = [1,2,3,4,5,9,8,7,6,10,23,45,65,24,21]
# max_score = 0
# for i in b :
# 	if i > max_score:
# 		max_score = i


# print (max_score)
# print(max(b))
# print

# print ("Program to prim the sum of the number untill reached")
# user_input = int(input("enter the number upto which you would like to sum upto : \n"))

# a = 0
# snum = 0
# while a <= user_input:
# 	snum += a 
# 	a += 1 

# print (snum)

# snum2 = 0

# b = range(1,101,+1)
# for i in b:
# 	snum2 += i

# print(snum2)
# print (a)
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# num = ["1","2","3","4","5","6","7","8","9","0"]
# symbols = ["!","@","#","%","^"]


# letter = int(input("How many letters do you want ?\n "))
# digits = int(input("How many digits do you want ?\n "))
# symbol_n= int(input("How many digits do you want ?\n "))
# total_len = 0
# password = []
# for i in range(0,letter + 1):
# 		random_letter = random.choice(alphabet)
# 		print (random_letter)
# 		password.append(random_letter)
# for i in range (0,digits + 1):
# 		random_digit = random.choice(num)
# 		password.append(random_digit)
# 		print (random_digit)
# while i < symbol_n:
# 		random_symbol = random.choice(symbols)
# 		password.append(random_symbol)
# 		print(random_symbol)
# 		i += 1
# random.shuffle((password))
# print("".join(password))
# random.shuffle((password))
# print(password)
# nospaces = ""
# for a in password:
# 	nospaces += a
# print(nospaces)


# for i in range(0,letter):
# 	password += random.choice(alphabet)
# for i in range(0,digits):
# 	password += random.choice(num)
# for i in range(0,symbol_n):
# 	password += random.choice(symbols)

# print (password)
# import random
# words = [
#     "apple", "grape", "mango", "pearl", "stone", "plant", "chair", "table", "house", "river",
#     "eagle", "tiger", "zebra", "sheep", "goose", "flame", "smile", "laugh", "storm", "cloud",
#     "ocean", "beach", "shore", "field", "earth", "grass", "lemon", "berry", "peach", "melon",
#     "piano", "flute", "drums", "viola", "cello", "harps", "books", "pages", "novel", "story",
#     "light", "shade", "color", "black", "white", "green", "brown", "cream", "blood", "heart",
#     "brain", "teeth", "hands", "knees", "elbow", "spine", "touch", "sight", "sound", "voice",
#     "dream", "sleep", "awake", "night", "brown", "sunny", "rainy", "windy", "snowy", "frost",
#     "queen", "crown", "sword", "shield", "armor", "giant", "fairy", "witch", "ghost", "robot",
#     "alien", "space", "orbit", "stars", "comet", "music", "dance", "paint", "craft", "build",
#     "write", "study", "learn", "teach", "games", "bread", "milky", "honey", "knife", "spoon",
#     "water", "fruit", "grill", "flour", "sugar", "pasta", "cheese", "toast", "cakes", "berry"
# ]


# selected_word = random.choice(words)
# lives = 6
# length = len(selected_word)
# print(selected_word)
# blank = []
# selected_word = list(selected_word)

# for b in range(length):
# 	blank += "_"
# print ("".join(blank))
# while lives > 0:
# 		userinput = input("enter your guess : \n ".lower())
# 		correct = False
# 		for a in range(length):
# 			if userinput == selected_word[a]:
# 				blank[a] = userinput
# 				correct = True
# 		print (("".join(blank)))
# 		if correct == True:
# 			print(f"You Guessed a right letter \n You have {lives} remaining")
# 		else:
# 			lives -= 1
# 			print(f"you Guessed a wrong letter\n You have {lives} lives remaining")
# 		if blank == selected_word:
# 			print ("You gussed the word")
# 			break
# if lives == 0 and blank != selected_word:
# 	print (f'You Lost , The word was {"".join(selected_word)}')

# while lives > 0:
# 	correct = False
# 	userinput = str(input("enter your first guess : ").lower())
# 	if userinput == word[0]:
# 		blank[0] = userinput
# 		correct = True	
# 	if userinput == word[1]:
# 		blank[1] = userinput
# 		correct = True	
# 	if userinput == word[2]:
# 		blank[2] = userinput
# 		correct = True	
# 	if userinput == word[3]:
# 		blank[3] = userinput
# 		correct = True	
# 	if userinput == word[4]:
# 		blank[4] = userinput
# 		correct = True	
# 	if correct == True:
# 		print("you guessed a right letter")
# 	else:
# 		print(f"You gussed a wrong letter \n Lives remaining = {lives - 1}")
# 		lives -= 1
# 	print (blank)
# 	if blank == word:
# 		print("you guessed the word right")
# 		break
# print("Game Over")