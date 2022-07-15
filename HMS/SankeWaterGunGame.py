import random


def SWGgame(turns):
    userScore = 0
    computerScore = 0
    while turns:
        l = ["S","W","G"]
        computerChoice = random.choice(l)
        userChoice = input("\nEnter Your Choice : ")
        if computerChoice == userChoice:
            print("This is a Draw \nTurns left ",turns-1)
        elif computerChoice=="S" and userChoice=="W":
            computerScore += 1 
            print("Computer Wins\nTurns left",turns-1)
        elif computerChoice=="S" and userChoice=="G":
            userScore += 1
            print("User Wins \nTurns left ",turns-1)
        elif computerChoice=="W" and userChoice=="G":
            computerScore += 1
            print("Computer Wins\nTurns left",turns-1)
        elif computerChoice=="W" and userChoice=="S":
            userScore += 1
            print("User Wins \nTurns left ",turns-1)
        elif computerChoice=="G" and userChoice=="S":
            computerScore += 1 
            print("Computer Wins\nTurns left",turns-1)
        elif computerChoice=="G" and userChoice=="W":
            userScore += 1
            print("User Wins \nTurns left ",turns-1)      
        else:
            print("Invalid Option Choosen !-----> Turns left",turns)
            turns += 1
        turns -= 1
        
    print("\nTotal Computer Score : ",computerScore)
    print("Total User Score : ",userScore)
    if computerScore > userScore:
        print("Computer Wins !")
    elif userScore > computerScore:
        print("User Wins !")
    else:
        print("Its a Draw !")

                    
print("----->Welcome to SNAKE WATER GUN game<------")
print("Game Rules \nSelect \"S\" for Snake\nSelect \"W\" for Water\nSelect \"G\" for Gun")

playAgain = 1
while playAgain:
    turns = int(input("Enter No of turns you want to play : "))
    SWGgame(turns)
    playAgain = int(input("Do You want to play again ? 1.Yes 0.NO\n"))

