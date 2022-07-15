#file IO Basics
"""
"r" - Open file for reading
"w" - Open file for writing
"x" - Create file if not exists
"a" - Add more content to a file
"t" - Text mode
"b" - Binary Mode
"+" - Read and Write
"""

from asyncore import read
from importlib.resources import contents

# REading Methods
# f = open("Dhiraj.txt","r")
# print(f.readline())
# print(f.readline())
# print(f.readlines())

# for line in f:
#     print(line, end="") 
    
# contents = f.read()
# print(contents)
# f.close()

#Wrtting Methods
# f = open("writing.txt","w")
# f.write("I am writing The file\n")
# a = f.write("This is second Line\n")
# print(a)

# f = open("writing.txt","r+")
# print(f.read())
# f.write("This is apending in the file")
# f.close()

with open("Dhiraj.txt") as f:
    a = f.read()
    print(a)
    
f = open("Dhiraj.txt")
a= f.read()
print(a)
f.close()
