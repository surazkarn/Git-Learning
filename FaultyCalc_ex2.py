"""
Scenario:
Suppose that you are an invigilator in an exam. A calculator is not allowed for the exam. You discover somehow that students are 
planning to cheat in exams, using a calculator program in Python language. Somehow, you get your hands on the calculator program. 
Now you want to alter a few results in the calculator with your own provided results to catch the students trying to cheat using the 
calculator program.The user will provide the following inputs:

Operator
The two numbers between which the operator is applied

All the results will be correct, except for these few:
45 * 3 = 555
56+9 = 77
56/6 = 4
"""

op = input("Enter operand : ")
a = int(input("Enter 1st number : "))
b = int(input("Enter second number : "))
if op=='*':
    if a==45 and b==3:
        print(555)
    else:
        print(a*b)
elif op=='+':
    if a==56 and b==9:
        print(77)
    else:
        print(a+b)
        
elif op=='/':
    if a==56 and b==6:
        print(4)
    else:
        print(a/b)
else:
    print("Enter valid operator !")
    


