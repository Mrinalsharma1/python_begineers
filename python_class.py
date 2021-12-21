# get value by class name
class myclass:
    x = 5


print(myclass.x)


# get value by object name
class myclass:
    x = 5


p1 = myclass()
print(p1.x)

# creat a class
# class vicle:
#     att1 = "bmw"
#     att2 = "Tata"

#     def myfun(self, a, b):
#         print(a, self.att1)
#         print(b, self.att2)


# x = str(input("enter your name  "))
# y = int(input("enter your age  "))
# obj1 = vicle()
# # print(obj1)
# obj1.myfun(x, y)

# A Sample class with init method
class person:
    def __init__(self, name) -> None:
        self.name = name

    def say_hi(self):
        print("hello, my name is", self.name)


p = person("mrinal")
p.say_hi()

# python exercise
class cal:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def cal1(self):
        sum = self.x * self.y
        if sum > 1000:
            add = self.x + self.y
            return add
        else:
            mul = self.x * self.y
            return mul


a = int(input("enter first number"))
b = int(input("enter second number"))
obj1 = cal(a, b)
print(obj1.cal1())
