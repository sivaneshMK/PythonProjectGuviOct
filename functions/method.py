
print(4+4)

print(4+7+7+8)

number = [73, 833, 8393, 83993, 8383, 83]
total = 0
for n in number:
    total+=n

print(total)

number1 = [8393, 83434, 8393, 33, 9393, 83939]

for n in number1:
    total+=n

print(total)

'''
Method or functions
Method is a set of program or set of statement grouped togather to perform some functions

2 different types of method
    1. user defined method
    2. in build methods

when your calling the method then only the statements which is there in the method will be executed

method will be executed when your calling


syntax 

def identifier(parameters):
    statement


parameters --> input

why
-----

reuse the statement or program


'''

# def add():
#     print(5+4)

# a, b is a parameters
# where your calling the method there you have to pass value to the each parameters
# def add(a, b, c, d):
#     print(a+b+c+d)

def add(*value):
    total = 0
    print(value)
    print()
    for a in value:
        print(a)
        for i in a:
            print(i)
            total+=i
    return total


def sub(a, b):
    print(a-b)

def div(nume=0 , den=1):
    print(nume/den)

def mul():
    print(5*4)

def avg(total_mark, total_num_sub):
    return total_mark / total_num_sub
    #print()

# add(4,8)
# sub()
# div()
# add(8,7)
# add(55, 8)
# add(738, 8383)
#add(738, 8383, 73, 83933, 83833, 839393,  7223823,7282374833, 728227274434)
#add(f=9, a=8)


marks = {"prince":[83, 73, 83, 93, 84], "vidhya":[78, 92,100, 93, 90], "Varshni":[80,86,91,92,75]}

for std in marks:
    std_mark = marks[std]
    total_mark =add(std_mark)
    print(total_mark)
    print(avg(total_mark, len(std_mark)))

sub(5,6)
div()