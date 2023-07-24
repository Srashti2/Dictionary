
print("Welcome to the auction world")

bidding={}

def auction():
    name = input("What is your name? : ")
    bid= int(input("What is your bid?: " ))
    bidding[name]=bid
    print(bidding)

def members():
    member =input("Are there any other member?: ").lower()
    if member=="yes":
        auction()
        members()
    else:
        highest=max(bidding.values())
        print("Highest bidder is : ",list(bidding.keys())
              [list(bidding.values()).index(highest)])
        print(f"Highest bid is :{highest}")



auction()
members()
