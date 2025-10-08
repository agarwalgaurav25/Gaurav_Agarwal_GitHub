#Black Jack
import random

deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_hand = []
comp_hand =[]
user_sum = sum(user_hand)
comp_sum = sum(comp_hand)

def initial_hand():
    for i in range(2):
        user_hand.append(random.choice(deck))
        comp_hand.append(random.choice(deck))
    if user_sum > 21:
        print ("USer Lost")
        quit()
    elif comp_sum > 21:
        print ("User Win")
        quit()

def display_hands():
    print(f'User has : {user_hand}')
    print(f'Comp has :{comp_hand}')

# def ace():
#     if "A" in user_hand:
#         input("use Ace as 1 or 11")

initial_hand()
display_hands()


def does_dealer_need_another_card(dealer_hand):
    sum_dealer_hand = sum(dealer_hand)
    if sum_dealer_hand <17:
        dealer_hand = list(dealer_hand)
        dealer_hand.append(random.choice(deck))

   
def check_who_won():
    display_hands()
    if user_sum > 21:
        print ("USer Lost")
        quit()
    elif comp_sum > 21:
        print ("User Win")
        quit()
    elif user_sum == comp_sum:
        print("It is a draw")
        quit()   
    elif (user_sum) > (comp_sum):
        print (f"User wins")
        quit()
    elif user_sum< 21:
        user_choice = (input("Would You like to hit ? enter y for yes , n for no")).upper()
    else:
        print("User Lost")
        quit()
    return user_choice
   
while check_who_won() == "Y":
    does_dealer_need_another_card(comp_hand)
    new_card = random.choice(deck)
    if user_sum > 11 and new_card == 11:
        user_sum += 1
    else:
        user_hand.append(new_card)
    check_who_won()
    
   



    
    
