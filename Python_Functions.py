# create function
def myfunction():
    print(" hey this is python")


myfunction()
myfunction()

# argumented function
def myfunction(x):
    print(x + " hey this is python")


myfunction("mrinal")
myfunction("sagar")

# This function expects 2 arguments, and gets 2 arguments:


def sum(x, y):
    add = x + y
    return add


num1 = 12
num2 = 18
print("two no is", sum(num1, num2))

# This function expects 2 arguments from user, and gets 2 arguments:


def sum(x, y):
    add = x + y
    return add


# num1 = int(input("Enter Frist Number"))
# num2 = int(input("Enter Second Number"))
print("two no is", sum(num1, num2))


# This function expects arguments from user, and gets 2 arguments and if arguments are not inserted bydefault value are set that time:


def sum(country="india"):
    return country


sum("bharat")
sum("brazil")
# shgghsgh
sum()
sum("texus")

print("country name is", sum(num1))

# Passing a List as an Argument
def fruit(food):
    for x in food:
        print(x)


name = ["apple", "banana", "guava"]
fruit(name)

# Passing a tupple as an Argument
def fruit(food):
    for x in food:
        print(x)


name = ("apple", "banana", "guava")
fruit(name)

# recursion
def my_rec(k):
    if k > 0:
        print(k)
        result = k + my_rec(k - 1)
        print(result)
    else:
        result = 0
    return result


print("recursion example result")
my_rec(6)

# first n natural number
def my_nat(x):
    if x > 0:
        sum = x + my_nat(x - 1)
        return sum
    else:
        sum = 0
        return sum


print("sum of n number is")
a = int(input("enter number"))
print("sum of the number is:", my_nat(a))
