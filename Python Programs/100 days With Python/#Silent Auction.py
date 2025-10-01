#Silent Auction

#Uncomment line13 - if you want the the first bidder to win incase they place the same bid
#if you want the both to win - leave it commented

print(r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\ ''')
more_users = "yes"
all_bids={}
print("\n" * 3 )
print("     Welcome to the silent Auction \n    Please start placing you bids")
def find_the_highest_bidder(bids):
        highest_bid=max(bids.values())
        for key in bids:
            if bids[key] == highest_bid:
                print (f"{key} had the highest bid ")
                # break #Uncomment if you want the first bidder with

while more_users == "yes":
    name= input("Enter your name : ").upper()
    bid = int(input("enter you bid : $"))
    all_bids[name]= bid
    more_users= input("Type 'yes' if more users left ").lower()
    print("\n" *100)

print(all_bids)   


# print(f'The max bid was {max_bid}')
find_the_highest_bidder(all_bids)

