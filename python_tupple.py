# decleraction of tupple
mytupple = ("hey", "you", "whats", "up")
print(mytupple)

# know tupple length
print(len(mytupple))

# kown tupple valure by index
print(mytupple[1])

# for loop in tupple
for x in mytupple:
    print(x)

# for loop in tupple to check value is exixt in tupple or not
for x in mytupple:
    if "you" in x:
        print("yes  " + x + "  is avalible")

# Convert the tuple into a list to be able to change it:
y = list(mytupple)
y[3] = "mrinal"
mytupple = tuple(y)
print(mytupple)

# Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

# Convert the tuple into a list, remove "apple", and convert it back into a tuple:
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# The del keyword can delete the tuple completely:
del thistuple
# thistuple = ("hey")
# print(thistuple)

# Unpacking a tuple:
fruits = ("apple", "banana", "cherry")
(green, yellow, white) = fruits
print(green)
print(yellow)
print(white)

# Assign the rest of the values as a list called "white":
fruits = ("apple", "banana", "cherry", "banana", "cherry")
(green, yellow, *white) = fruits
print(green)
print(yellow)
print(white)

# Multiply the fruits tuple by 2:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
