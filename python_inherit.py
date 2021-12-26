# python inherite start here
# Create a class named Person, with firstname and lastname properties, and a printname method:
class person:
    def __init__(self, fname, lname):

        self.x = fname
        self.y = lname

    def printname(self):
        print(self.x, self.y)


p = person("mrinal", "sharma")
p.printname()

# inheritance is  there
class animal:
    # def __init__(self,parrot) -> None:
    #     self.x = parrot

    def bird(self):
        print("this is a bird")


class wild(animal):
    # def __init__(self,lion) -> None:
    #     self.y = lion

    def ani(self):
        print("this is  animal")


obj = wild()
obj.bird()
obj.ani()

# multiple inheritance
class animal:
    def speak(self):
        print("animal is speaking")


class dog(animal):
    def bark(self):
        print("this is dog")


class cat(dog):
    def run(self):
        print("this is cat")


obj1 = cat()
print(" ******  multiple inheritance is there   ******")
obj1.speak()
obj1.bark()
obj1.run()

# use init() function in base class


class person:
    def __init__(self, fname, lname):
        self.name = fname
        self.sname = lname

    def printkro(self):
        print(self.name, self.sname, self.age)

    def printkro1(self):
        print(self.name, self.sname)


class c1(person):
    def __init__(self, fname, lname, age):
        person.__init__(self, fname, lname)
        self.age = age


class c2(person):
    def __init__(
        self,
        fname,
        lname,
    ):
        super().__init__(fname, lname)


obj1 = c1("mrinal", "kumar", "2000")
obj2 = c2("sagar", "sharma")
obj1.printkro()
obj2.printkro1()
