'''
Operator overloading
+ - * /  ect
'''


class Student():

    def __init__(self, marks):
        self.marks = marks


    def __add__(self, other):
        return self.marks-other.marks

s1= Student(50)
s2 = Student(60)

print(s1+s2)


'''
s1.__add__(s2)

self.marks= 50
other.marks = 60




'''