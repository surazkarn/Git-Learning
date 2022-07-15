"""
Instructions:
Create a food log file for each client
Create an exercise log file for each client.
Ask the user whether they want to log or retrieve client data.
Write a function that takes the user input of the client's name. After the client's name is entered, it will display a message as "What you want to log- Diet or Exercise".
Write a function to retrieve exercise or food file records for any client.
"""

def getdate():
           import datetime
           return datetime.datetime.now()
       
def log():
    clientname = input("Enter Client Name :\n 1.Harry\n 2.Ram\n 3.Shyam\n")
    looping = 1
    if clientname == "Harry":
        while looping==1:
            clientChoice = int(input("What you want for Harry to log on :\n 1.diet\n 2.exercise\n")) 
            if clientChoice == 1:
                f = open("Harry_diet.txt","a")
                print("Enter Diet You have Taken : ")
                f.write(str([str(getdate())])+" "+input()+"\n")
                f.close()
            
            elif clientChoice==2:
                f = open("Harry_exercise.txt","a")
                print("Enter Exercise You have Done : ")
                f.write(str([str(getdate())])+" "+input()+"\n")
                f.close()
            
            else:
                print("Invalid Choice !")
            looping = int(input("Do you want to continue : 1.Yes 2.No\n"))
        
    elif clientname == "Ram":
        while looping==1:
            clientChoice = int(input("What you want for Ram to log on :\n 1.diet\n 2.exercise\n")) 
            if clientChoice == 1:
                f = open("Ram_diet.txt","a")
                print("Enter Diet You have Taken : ")
                f.write(str([str(getdate())])+" "+input()+"\n")
                f.close()
            
            elif clientChoice==2:
                f = open("Ram_exercise.txt","a")
                print("Enter Exercise You have Done : ")
                f.write(str([str(getdate())])+" "+input()+"\n")
                f.close()
            
            else:
                print("Invalid Choice !")
            looping = int(input("Do you want to continue : 1.Yes 2.No\n"))
        
    elif clientname == "Shyam":
        while looping==1:
            clientChoice = int(input("What you want for Shyam to log on :\n 1.diet\n 2.exercise\n")) 
            if clientChoice == 1:
                f = open("Shyam_diet.txt","a")
                print("Enter Diet You have Taken : ")
                f.write(str([str(getdate())])+" "+input()+"\n")
                f.close()
            
            elif clientChoice==2:
                f = open("Shyam_exercise.txt","a")
                print("Enter Exercise You have Done : ")
                f.write(str([str(getdate())])+" "+input()+"\n")
                f.close()
            
            else:
                print("Invalid Choice !")
            looping = int(input("Do you want to continue : 1.Yes 2.No\n"))
        
    else:
        print("Invalid Client Name ! ")

def retrieve():
    looping = 1
    while looping == 1:
        clientname = input("Enter Client Name :\n 1.Harry\n 2.Ram\n 3.Shyam\n")
        if clientname == "Harry":
            clientChoice = int(input("What data You want to retrieve : \n 1.Diet \n 2.Exercise\n"))
            if clientChoice == 1:
                with open("Harry_diet.txt") as f:
                    print(f.read())
            
            elif clientChoice == 2:
                with open("Harry_exercise.txt") as f:
                    print(f.read())
            
            else:
                print("Invalid Choice !")

        elif clientname == "Ram":
            clientChoice = int(input("What data You want to retrieve : \n 1.Diet \n 2.Exercise\n"))
            if clientChoice == 1:
                with open("Ram_diet.txt") as f:
                    print(f.read())
            
            elif clientChoice == 2:
                with open("Ram_exercise.txt") as f:
                    print(f.read())
            
            else:
                print("Invalid Choice !") 
                
        elif clientname == "Shyam":
            clientChoice = int(input("What data You want to retrieve : \n 1.Diet \n 2.Exercise\n"))
            if clientChoice == 1:
                with open("Shyam_diet.txt") as f:
                    print(f.read())
            
            elif clientChoice == 2:
                with open("Shyam_exercise.txt") as f:
                    print(f.read())
            
            else:
                print("Invalid Choice !") 
        looping = int(input("Do You want to continue : 1.Yes 2.No\n"))

print("----->Welcome To Hotel Management System<-----")
userChoice = int(input("Enter Your Choice for Client Data :\n 1.Log\n 2.Retrieve\n"))
if userChoice == 1:
    log()
elif userChoice == 2:
    retrieve()
else:
    print("Enter Valid Choice ! ")
            