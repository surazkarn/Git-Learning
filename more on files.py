f = open("Dhiraj.txt","r")
print(f.readline()) #read line by line
print(f.tell()) #tell where the pointer is in file
f.seek(0) #brings the pointer to the given index
print(f.readline())
f.close()