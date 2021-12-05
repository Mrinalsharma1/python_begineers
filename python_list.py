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

# just for updating once again 1

# loop start
ilist = ["one", "two", "three"]
for x in ilist:
    print(x)

# loop with range and len
# ilist = ["apple", "banana", "cherry", "one", "three", "two"]
# for i in range(len(ilist)):
#     print(ilist[i])

# whilw loop
# ilist = ["apple", "banana", "cherry", "one", "three", "two"]
# i = 0
# while i < len(ilist):
#     print(ilist[i])
#     i = i+1


# python_lists_comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
        print(newlist)

# python short alphabet
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits.sort()
print(fruits)

# python sort number
num = ["70", "20", "90", "40", "10"]
num.sort()
print(num)

# python sort number by reverse order
num = ["70", "20", "90", "40", "10"]
num.sort(reverse=True)
print(num)

# Sort the list based on how close the number is to 50:


def myfun(n):
    return abs(n - 50)


num = [100, 50, 30, 40, 50, 120, 300, -0, -300, 45, 20]
num.sort(key=myfun)
print(num)


# Reverse the order of the list items:
check = ["hy", "hello", "may", "might", "should"]
check.reverse()
print(check)

# Make a copy of a list with the list() method:
clist = ["abc", "def", "jhi", "jkl", "mno", "pqr"]
# mylist = clist.copy() this is a one way to copy list
mylist = list(clist)  # this is a second way to copy list
print(mylist)

# join two list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# add list 2 in list 1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)

# add list 1 in list 2
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list1:
    list2.extend(x)
print(list2)
