
class Demo:
    # class level variable
    v=10

# class leve variables or methods can be called by using class name reference

print(Demo.v)

class Demo1:

    @staticmethod
    def value():
        print(Demo.v)


Demo1.value()
