# Create and print a dictionary:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# Print the "brand" value of the dictionary:

print(thisdict["year"])

# Duplicate values will overwrite existing values:
dupl = {
    "fruits": "apple",
    "car":  "bmw",
    "cloth": "pant",
    "fruits": "mango"
}
print(dupl)

# Print the number of items in the dictionary:
print(len(dupl))

# String, int, boolean, and list data types:

datatype = {
    "color": ["red", "green", "blue"],
    "fruit": ("apple", "banana", "guava"),
    "car": {"bmw", "swift", "tata"},
    "name": "mrinal",
    "number": 345
}
print(datatype["color"])

# print all the value
print(datatype.values())

# Change the "year" to 2018:
change = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
change["year"] = 7787
print(change)

# The pop() method removes the item with the specified key name:
change.pop("model")
print(change)

# The del keyword removes the item with the specified key name:
# del change

# The clear() method empties the dictionary:
change.clear()
print(change)

# Print all key names in the dictionary, one by one:

loop1 = {
    "name": "mrinal",
    "roll": 55,
    "phone": 787031001
}
for x in loop1:
    print(x)

# copy dictonary
loop2 = loop1.copy()
print(loop2)

# Create a dictionary that contain three dictionaries:
family = {
    "child1": {
        "child11": {
            "name": "ramesh",
            "age": 20,
            "city": "patna"
        },

    },
    "child2": {
        "name": "raju",
        "age": 23,
        "city": "bala"
    },
    "child3": {
        "name": "mohan",
        "age": 25,
        "city": "gujar"
    },
}
print(family)
print(family["child1"]["child11"]["name"])
