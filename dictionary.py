# d1 = {"dhiraj":"bhat","suraj":"dal",
#       "chandan":1200, 40:"papa"}
# print(d1)
# print("\n")
# print(d1.keys())
# print(d1.values())
# d1["babu"] = 5
# d1.update({"xote":5})
# print(d1)
# del d1["babu"]
# print(d1)
# #making copies

# d2 = d1.copy()
# del d2["xote"]
# print(d1)
# print(d2)

# nested dictoinary
d1 = {"dhiraj":"bhat","suraj":"dal",
      "chandan":1200, 40:"papa",
      "nested":{"a":"apple", "b":"ball"}}
print(d1)
print(d1["nested"]["a"])
print(d1.get("dhiraj"))
