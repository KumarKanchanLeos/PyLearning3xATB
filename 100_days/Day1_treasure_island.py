print("welcome to Treasure Island")
print("your mission is to find the Treasure")
choice1= input('you\'re at crossroad,where do you want to go?Type "left" or "right" \n').lower()

if choice1 =="left":
    choice2=input('you have come to the middle of the island.'
     'You want to "swim" or "wait"?').lower()
    if choice2== "wait":
        choice3= input("please tell which colour door you choose.red,yellow or blue").lower()
        if choice3 == "red":
            print("Game Over")
        elif choice3==  "blue"  :
            print("Game Over")
        elif choice3 =="yellow":
            print("Hurrey! you won")
        else:
            print("YOU CHOOSE THE INVALID DOOR.Game over")
    else:
        print("you got attacked by angry trout.Game over")
if choice1 == "right":
    print("You fell into a hole and fell over.Game Over")
else:
    print("Game Over")