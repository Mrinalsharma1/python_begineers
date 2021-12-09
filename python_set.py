# Create a Set:

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Loop through the set, and print the values:
set1 = {"this", "is", "a", "good", "boy"}
for x in set1:
    print(x)

# Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# Add an item to a set, using the add() method:
thisset.add("guava")
print(thisset)

# Add elements from tropical into thisset:
thisset = {"apple", "banana", "cherry"}
thisset1 = {"this", "is", "a", "good", "boy"}
thisset.update(thisset1)
print(thisset)

# Add elements of a list to at set:
hey = ["hey", "i", "am", "mrinal"]
thisset.update(hey)
print(thisset)

# remove value in set
thisset = {"apple", "banana", "cherry"}
thisset.remove("apple")
print(thisset)

# The union() method returns a new set with all items from both sets:
set1 = {"a", "b", "c"}
set2 = {"d", "e"}
set1.update(set2)
set3 = set1.union(set2)
print(set1)
print(set3)

# just for fun
