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
