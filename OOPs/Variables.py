'''
class level variable
instance variable
local variable
global variable

'''

class var:

    def __init__(self):
        # instance variable
        self.c = 100
        self.d = 103

    # class level variable
    a = 10

    @classmethod
    def class_method(cls):
        #local variable
        b =30
        print(cls.a)
        print(b)

    @staticmethod
    def method():
        print(var.a)
        z = var()
        print(z.c)
        print(z.d)

    def instance_method(self):
        print(var.a)
        print(self.d)
        print(self.c)

        global s
        s = 10





print(var.a)
var.class_method()

print()
v = var()
v.instance_method()
print(v.c)
print(v.d)
print("s", s)


''''
Interface abc():

class xyz() implements abc{

}

class bc() implements abc{


}

class by(){ 

abc a;

method(){
   a = new xyz();
    
}

method2(){
    a = new bc();
}


}





'''