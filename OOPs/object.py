
class Demo:
    # class level variable
    v=10

# class leve variables or methods can be called by using class name reference
# the static methods are executed only once during the execution
# When the classloader program is executed at that time the static method will executed

# in a class if you have static and instance methods
# the static method will be executed first

print(Demo.v)

class Demo1:

    @staticmethod
    def value():
        print(Demo.v)


Demo1.value()
