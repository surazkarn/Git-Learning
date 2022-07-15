# create a dictionary take input from the user and show the meaning of the key from the dictionary
dict = {"apple":"An apple is a fruit",
        "mutable":"Something that can be changed",
        "immutable":"Something that cannot be changed",
        "links":"https://www.wikipedia.org/"}

searching = input("Enter word to search : ")
# print(dict.get(searching))
print(dict[searching])