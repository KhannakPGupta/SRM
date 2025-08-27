#ROCK PAPER SCISSORS GAME

#Importing random module to let the computer choose randomly
import random


#Function to display the rules of the game
def rules():
    print("\n🎮 Welcome to Rock-Paper-Scissors!🎮\n")
    print("========Rules=========")
    print("👉 Rock beats Scissors")
    print("👉 Paper beats Rock")
    print("👉 Scissors beats Paper")
    print("\nLet's see if you can beat the computer!\n")


#Fuction to display the menu of the game 
def menu():
    print("\nHERE ARE YOUR OPTIONS - ")
    print("1. Rock 🪨")
    print("2. Paper 📄")
    print("3. Scissors ✂️")
    print("4. Exit\n")


#Function which displays the computer's choice
def computer_choice():
    if comp_choice==1:
        print("\nComputer chose - Rock")
    elif comp_choice==2:
        print("\nComputer chose - Paper")
    elif comp_choice==3:
        print("\nComputer chose - Scissors")


#Function to display final scores and winner after user chooses to exit the game
def end_of_game():
    print("--------------------------------------------")
    print("\nThank you for playing with us!\n")
    print("THE FINAL SCORE IS - ")
    print("You scored", user_score, "points!")
    print("Computer scored", comp_score, "points!")


#Function to calculate the final winner based on final scores
def final_winner():
    if user_score>comp_score:
        print("\nCONGRATULATIONS! YOU ARE THE ULTIMATE WINNER 🥳")
    elif user_score==comp_score:
        print("\nYOUR SCORES ARE EQUAL. IT'S A TIE!")
    elif user_score<comp_score:
        print("\nOOPS! THE COMPUTER IS THE ULTIMATE WINNER. BETTER LUCK NEXT TIME! 🤖")


#Initialising user and computer score as zero
user_score = 0
comp_score = 0


#Calling the rules function to display the instructions before the game begins
rules()


#Using a while loop so that game continues after each round
while True:
    try:
        #Calling the menu function to display options 
        menu()


        #Taking user's input
        user_choice = int(input("Enter your choice (1,2,3 or 4) : "))


        #Selecting random computer choice and then calling the function to display it
        comp_choice=random.choice([1,2,3])
        computer_choice()


        #Condition when both select the same thing, resulting in a tie
        if user_choice==comp_choice:
            print("\nIt's a tie this round!\n")


        #Conditions when user wins over computer
        elif (user_choice==1 and comp_choice==3) or (user_choice==2 and comp_choice==1) or (user_choice==3 and comp_choice==2):
            #increment user's score and display it along with winning message
            user_score+=1
            print(" \n🎉 You win this round!\n")
            print("Your score is : ", user_score)
            print("Computer's score is : ", comp_score)


        #Condition when user chooses to exit the game - call funtions end of game and final winner
        elif user_choice==4:
            end_of_game()
            final_winner()
            break          #Moving out of the loop when exit is selected


        #Condition when computer wins over user
        elif (user_choice==1 and comp_choice==2) or (user_choice==2 and comp_choice==3) or (user_choice==3 and comp_choice==1):
            #increment computer's score and display is along with losing message
            comp_score+=1
            print(" \n🤖 Computer wins this round!\n")
            print("Your score is : ", user_score)
            print("Computer's score is : ", comp_score)


    #Exception handling when invalid option is selected
    except:
        print(" ❌ ERROR - Please enter a valid option!")
    