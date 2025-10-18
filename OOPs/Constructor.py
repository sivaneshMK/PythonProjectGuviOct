

class Calculator:

    def __init__(self):
        print("This is a constructor")
    # instance contents or called as object level content
    #instance methods
    def add(self, *args):
        total =0
        for i in args:
            total+=i
        return total

    def sub(self, a):
        return a- self.add(1, 2, 3, 4)

abcd = Calculator.add(3, 4, 5, 66)
print(abcd)


# to call the instance method you have to use object reference
#print(Calculator.sub(4))

# syntax to create object
# identifier = constructor_name()
# constructor name should be same classname
calc = Calculator()
print(calc.sub(4))

''''
constructor ---> constructor will construct the instance content of the class
when creating an object

types
---------
default constructor
perameterized constructor

how the construct
-------------------
constructor will also look like a method
but it wont have any name. it will be accessed by using class name
it will be declared by using def __init__(self):

constructors can't be called explictly
but it will be accessed implicitly  when we are creating an object

it wont have any return type

if user is not created any constructor the compiler will create
constructor for the class in compile time it is called as default constructor

'''
