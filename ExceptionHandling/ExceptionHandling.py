'''
Exceptions are like a unexpected scenario which raised during the runtime
it will terminate the program execution when it is raised

as a programmer we can handle certain exceptions by using
try, except and finally block

as a programmer we can also raise an exception to stop the execution

2types of exceptions in python
inbuild exceptions
user defined exceptions
'''

print("8393"+"here") # concadination
print(89393+88393) # addition
try:
    print("abcd"+8393)
except :
    print("your trying to concat string with integer")

try:
    print(int("akjsks"))
    print(5/0)
    print("abcd" + 8393)
except TypeError as typeerror:
    print("Type error")


except ZeroDivisionError as zero:
    print("denominator is zero")

except Exception:
    print("abcd")
    try:
        print(int("akjsks"))
    except:
        print("Value error inside the except block")

with open("..//file.txt") as file:
    data =file.readlines()
print(data)


try:
    a=[444, 5, 3,]
    print(a[2])
except:
    print("error in the list")
finally:
    a=10
    print("Finally block")




