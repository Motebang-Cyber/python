import random
import time
import datetime

def Game_Text(Balance = 100):
    print("Welcome to the slot machine Game!")
    print("Starting Credit")
    print("Current Balance is", Balance, "credits")
   
def logic(Balance, credit, Pick_Final_1, pick_Final_2, pick_Final_3, pick1, pickx):
    while Balance > 0:
        if credit > 0 and credit <= 10:
            print("Spinning...")
            print(pick1)
            if pick1 == pickx:
                print("Congradulations you have a jackpot")
                Balance = Balance + (credit*10)
                print("New Balance:",Balance, "credits")
                Play = input("Play again?(yes/no)")
                if Play == "yes":
                    continue
                else:
                    break
            elif pick1 == Pick_Final_1 and pick1 == pick_Final_2:
                print("You have won 3 times your bet")
                Balance = Balance + (credit*3)
                print("New Balance:",Balance, "credits")
                Play = input("Play again?(yes/no)") 
                if Play == "yes":
                    continue
                else:
                    break
            elif pick1 == Pick_Final_1 and pick1 == pick_Final_3:
                print("You have won 3 times your bet")
                Balance = Balance + (credit*3)
                print("New Balance:",Balance, "credits")
                Play = input("Play again?(yes/no)")
                if Play == "yes":
                    continue
                else:
                    break
            elif pick1 == pick_Final_2 and pick1 == pick_Final_3:
                print("You have won 3 times your bet")
                Balance = Balance + (credit*3)
                print("New Balance:",Balance, "credits")
                Play = input("Play again?(yes/no)") 
                if Play == "yes":
                    continue
                else:
                    break
            else:
                print("unforturnately you lost this round")
                Balance = Balance - (credit*10)
                print("New Balance:",Balance, "credits")
                Play = input("Play again?(yes/no)") 
                if Play == "yes":
                    continue
                else:
                    break
        else:
            print("The bet amount must be between 1 and 10 credits!")
    

def main():
    Balance = 100
    pickx = ["","",""]

    now = datetime.datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")

    items = ["Cherry", "Bell", "Lemon", "Bottle", "Pen"]

    pick1 = random.sample(items, 3)

    Game_Text(Balance)
   
    credit = int(input("Enter a bet amount from 1 to 10"))
    print("starting time is", date_time)

    pickx[0] = input("Enter your first item bet")
    pickx[1] = input("Enter your second item bet")
    pickx[2] = input("Enter your third item bet")

    pick_Final_1 = pickx[0]
    pick_Final_2 = pickx[1]
    pick_Final_3 = pickx[2]

    if pickx != "":   
        logic(Balance, credit,pick_Final_1, pick_Final_2, pick_Final_3, pick1,pickx)
    else:
        print("you need to enter Values to Bet with")

    print("Ending time is", date_time)

main()