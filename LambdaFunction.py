# def add(x,y):
#     return x+y

# minus = lambda x,y: x-y

# def sub(x,y):
#     return x-y

# print(add(5,4))
# print(minus(5,4))
# print(sub(5,4))

l = [[2,5],[4,2],[5,6]]
l.sort(key=lambda x:x[1], reverse=0)
print(l)