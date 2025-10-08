#Number Guessing Game
import random

print(
	'''
  ________                                 __  .__               _______               ___.                  
 /  _____/ __ __   ____   ______ ______  _/  |_|  |__   ____     \      \  __ __  _____\_ |__   ___________  
/   \  ___|  |  \_/ __ \ /  ___//  ___/  \   __\  |  \_/ __ \    /   |   \|  |  \/     \| __ \_/ __ \_  __ \ 
\    \_\  \  |  /\  ___/ \___ \ \___ \    |  | |   Y  \  ___/   /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ 
 \______  /____/  \___  >____  >____  >   |__| |___|  /\___  >  \____|__  /____/|__|_|  /___  /\___  >__|    
        \/            \/     \/     \/              \/     \/           \/            \/    \/     \/       ''')

COMP_CHOICE = random.randint(1,100)
HARD_LEVEL = int(10)
EASY_LEVEL = int(5)
IS_GAME_OVER = False
LIVES = 0
def set_difficulty():
	diff = (input("Enter diffuclty level - easy or hard \n")).lower()
	if diff == "easy":
		return EASY_LEVEL
	elif diff == "hard":
		return HARD_LEVEL
	else:
		return HARD_LEVEL
	
def check_answer(u_choice,c_choice):
	global LIVES
	lives = LIVES
	if u_choice > c_choice:
		print("Too high")
		lives -= 1
	elif u_choice < c_choice:
		print('too low')
		lives -= 1
	elif u_choice == c_choice:
		print ("You gussed it right")
		IS_GAME_OVER = True
	if (lives) == 0:
		print ("sorry you lost")
		print (f"The number was {c_choice}")
		IS_GAME_OVER = True

def play_game():
	LIVES = set_difficulty()
	is_game_over = False
	while is_game_over == False:
		user_choice = int(input("ENter you guess : "))
		check_answer(user_choice,COMP_CHOICE)
		print (f"lives remaining = {LIVES}")
		

play_game()
