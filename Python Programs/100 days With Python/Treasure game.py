print("Treasure Hunt Game ")
st1 = input("you are at a cross road . Which direction ? right or left ").upper()
print (st1)
if st1 == "RIGHT":
	st2 = input(" You are on the right track, wanna swim or get a boat ? ").upper()
else:
	print (" You landed in a ditch")
	quit()
if st2 == "BOAT":
	st3= str(input("Nice you took a boat, Wanna have some food or sleep ").upper())
else :
	print ("the water had crocs, you die ")
	quit()
if st3 == "FOOD":
	print (" You had the food and slept.")
else:
	print("You died of Hunger")
	quit()