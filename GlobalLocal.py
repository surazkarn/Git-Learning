x = 80

def func1():
    a = 5
    global x
    x = 20   #this x has now access to global variable x and x value is modified here
    print(a, x)
    
def func2():
    a = 20
    def func3():
        a = 50
        b = 20
        print(a, b)
    func3()
    print(a)
    print(x)
    
# func1()
func2()
