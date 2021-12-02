# list are allowed duplicate value
dlist = ["banana", "apple", "orange", "apple"]
print(dlist)

# length in list
llist = ["boy", "girl", "suraj", "monu"]
print(len(llist))

# negative indexing in list
nlist = ["one", "two", "three", "four"]
print(nlist[-1])

# replace with new value
rlist = ["ramu", "raju", "hero", "dps"]
rlist[0] = "ganesh"
print(rlist)

# replace multiple value
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# insert value
alist = ["boys", "gain", "dude", "origin"]
alist.insert(2, "raman")
print(alist)

# insert value in last of number
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# remove item in the list
rlist = ["one", "two", "three"]
rlist.remove("two")
print(rlist)

# remove item by index
ilist = ["one", "two", "three"]
ilist.pop(0)
print(ilist)

# clear the list
ilist = ["one", "two", "three"]
ilist.clear()
print(ilist)

# just for updating
