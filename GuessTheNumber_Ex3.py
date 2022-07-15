"""
You have to build a "Number Guessing Game," in which a winning number is set to some integer value. The Program should take input from the user, and if the entered number is less than the winning number, a message should display that the number is smaller and vice versa.
Instructions:
1. You are free to use anything we've studied till now.
2. The number of guesses should be limited, i.e (5 or 9).
3. Print the number of guesses left.
4. Print the number of guesses he took to win the game.
5. “Game Over” message should display if the number of guesses becomes equal to 0.
"""

ans = 55
noOfGuesses = 1

while(noOfGuesses<=5):
    num = int(input("Enter the Number : "))
    
    if num>ans:
        print("Please enter smaller number !\n")
    elif num<ans:
        print("Please enter greater number !\n")
    else:
        print("You Guessed The Answer, You win !\n")
        print("Guesses Used : ",noOfGuesses)
        break
    
    print("No of guesses left : ",5-noOfGuesses)
    noOfGuesses = noOfGuesses+1


if noOfGuesses==6:
    print("You Lose The Game !")
print("Game Over !")


   
        
    
