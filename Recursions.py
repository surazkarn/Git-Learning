def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    
    return fac

def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial_recursive(n-1)

def fibonacci_recursive(n):
    # if n==0 or n==1:         #for 0 indexed series
    if n==1 or n==2:           # for 1 indexed series
        return n-1
    
    return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)

# num = int(input("Enter num : "))
# print("factorial by iterative method : ",factorial_iterative(num))
# print("Factorial by recursive method : ",factorial_recursive(num))

fib = int(input("Enter ith term to print from fibonacci series : "))
print(fib,"th term in fibonacci is : ",fibonacci_recursive(fib))