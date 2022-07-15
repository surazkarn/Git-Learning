a = 5
b = 4

# print(sum((a,b))) #sum is inbuilt function
#user defined functions

def func1():
    print("This has no parameter passing")
def func2(a,b):
    # print("The sum of two number is : ",(a+b))
    return (a+b)
    
def func3(a,b):
    """This calculates the average of two numbers
        Use for two numbers only """
    average = (a+b)/2
    return average

func1()
print(func2(3,4))
print(func3(4,5))
print(func3.__doc__)