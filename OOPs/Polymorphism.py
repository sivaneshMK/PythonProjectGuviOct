'''
polymorphism
------------
if your doing the same function in multiple way it is called as
polymorphism

Travel to somewhere

1. walk
2. bus
3. cycle


1. method over loading
    in a same class if you declaring multiple methods with same name and
    different parameters or Arguments.
    method overloading is not supported in python

    how they are archiving method overloading



2. method overriding

    both parent and child classes have the same method with
    same name and same parameter list
    then the parent class method will be override by the child class method during the runtime







'''


class Calculator():

    def add(self, *args):
        total = 0
        for a in args:
            total += a

        print(total)

    def sub(self, c=0, d=0):
        print(c-d)

clac = Calculator()
clac.add(3, 4)




class Venkatachalam:

    def Bike(self):
        print("TVS XL")


class Karthic(Venkatachalam):

    def Bike(self):
        print("FZ")


kar = Karthic()
kar.Bike()

