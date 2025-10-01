import random
words = [
    "apple", "grape", "mango", "pearl", "stone", "plant", "chair", "table", "house", "river",
    "eagle", "tiger", "zebra", "sheep", "goose", "flame", "smile", "laugh", "storm", "cloud",
    "ocean", "beach", "shore", "field", "earth", "grass", "lemon", "berry", "peach", "melon",
    "piano", "flute", "drums", "viola", "cello", "harps", "books", "pages", "novel", "story",
    "light", "shade", "color", "black", "white", "green", "brown", "cream", "blood", "heart",
    "brain", "teeth", "hands", "knees", "elbow", "spine", "touch", "sight", "sound", "voice",
    "dream", "sleep", "awake", "night", "brown", "sunny", "rainy", "windy", "snowy", "frost",
    "queen", "crown", "sword", "shield", "armor", "giant", "fairy", "witch", "ghost", "robot",
    "alien", "space", "orbit", "stars", "comet", "music", "dance", "paint", "craft", "build",
    "write", "study", "learn", "teach", "games", "bread", "milky", "honey", "knife", "spoon",
    "water", "fruit", "grill", "flour", "sugar", "pasta", "cheese", "toast", "cakes", "berry"
]


selected_word = random.choice(words)
lives = 6
length = len(selected_word)

# #To check code - remove when checked : 
# print(selected_word)

blank = []
selected_word = list(selected_word)

for b in range(length):
	blank += "_"
print ("".join(blank))
while lives > 0:
		userinput = input("enter your guess : \n ".lower())
		correct = False
		for a in range(length):
			if userinput == selected_word[a]:
				blank[a] = userinput
				correct = True
		print (("".join(blank)))
		if correct == True:
			print(f"You Guessed a right letter \n You have {lives} remaining")
		else:
			lives -= 1
			print(f"you Guessed a wrong letter\n You have {lives} lives remaining")
		if blank == selected_word:
			print ("You gussed the word")
			break
if lives == 0 and blank != selected_word:
	print (f'You Lost , The word was {"".join(selected_word)}')
