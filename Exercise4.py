# Exercise 4
# Pattern Printing
# Input = Integer n
# Boolean = True or False

from re import I
from secrets import choice


row = int(input("Enter no. of rows : "))
print("Type 1 for Upper triangle part and 0 for Lower Triangle part")
choice = int(input())
choice = bool(choice)

if choice==True:
    for i in range(0,row+1): #row+1 is exclusive for it will consider 0 to 4 as needed
        for j in range(0,i): 
            print("* ",end="")
        print()

else:
    for i in range(row,0,-1): #-1 indicates decreasing 
        for j in range(0,i):
            print("* ",end="")
        print()
