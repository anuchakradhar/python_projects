name = input("Enter your name: ")
print(f"Welcome {name.capitalize()}, to this adventure!! ")


answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way you like to go?? ").lower()

if answer == 'left':
    answer1 = input("You came to a river, you can walk around it or swim across. Type your answer  walk or swim").lower()
    
    if answer1 == 'swim':
        print("You swam across and were eaten by an crocodile.")
    elif answer1 == 'walk':
        print("You walked for many miles, ran out of water and you lost the game..")
    else:
        print("Not a valid option. You lose")
            
elif answer == 'right':
    answer2 = input("You come to a bridge, it looks weak. Do you want to cross it or head back??(cross/back) ").lower()
    if answer2 == 'cross':
        answer3 = input("You crossed the bridge and meet a stranger. Do you want to talk to him(Yes/No)?? ").lower()
        if answer3 == "yes":
            print("You talked to the stranger. You get gift. You Won!!!")
        elif answer3 == "no":
            print("You got killed by stranger. You lose")
        else:
            print("Not a valid option. You lose..")

    elif answer2 == 'back':
        print("You turned back and lose.")
    else:
        print("Not a valid option. You lose")

else:
     print("Not a valid option. You lose")