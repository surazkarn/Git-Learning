s1 = set()
# print(type(s1))
# s1 = set([1,2,3,4])
l = [1,2,3,4]
s1 = set(l)
s1.add(5)
s1.add(3) #unique element will be kept only
s1.remove(3) #3 is removed
print("set1 : ",s1)
s2 = set([1,2,6,7,"a"])
print("set2 : ", s2)
print("union : ",s1.union(s2))
print("intersection : ",s1.intersection(s2))
print("difference : ", s1.difference(s2))
print("disjoint : ", s1.isdisjoint(s2))