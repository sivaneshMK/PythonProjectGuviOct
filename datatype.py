'''
int data
    arithmetic operators
    bit wise operators

float


Sequence --> list, tuple, string

'''

a = 99303933893989869.89398387998387938339393
print(type(a))
print(a)

'''
List --> sequence type 
used to store multiple values in sequence way
it will declared using []
each value separated with (,) 
there is no memory limitation(n no.of values)
it will follow the insertion order
each value in stored in different indexes 
indexes starts with 0
it will allow the duplicate
it will allow multiple type datas
list is mutable


'''


std_age = [22, 23, 4, 5, 88, 85, 39, 93, 33, 43, 39, 5,4, 22]

print(std_age)

std_age.append(97)
print(std_age)

print(std_age.pop())
print(std_age)

print(std_age[3])
print(std_age[5])
std_age.insert(4, 55)
print(std_age)
std_age.remove(55)
print(std_age)

'''
n--size 
-1 to find the n th value index

'''
std_age.reverse()
print(std_age)

'''
Slicing
[start: stop: step]
'''

print(std_age[0:4])
print(std_age)

print(std_age[1::2])
print(std_age[::2])
print(std_age[::3])
print(std_age[::-1])

print(std_age.index(88))
print(std_age.count(5))
print(std_age.extend([3833.8393, 8393, 833933.893, 83.8393]))
print(std_age)

print(std_age.sort())
print(std_age)
std_age.sort(reverse=True)
print(std_age)


'''
tuple
------
multiple type of values
it is immutable
+ve and -ve index
declare tuple ()
'''

mobile_number = (8393939333, 839399338933, 89274738, 74738392, 839399338933, 8833933)
print(mobile_number)
print(mobile_number[4])
print(mobile_number[-1])
# mobile_number[5] = "83830"
print(mobile_number)

print(mobile_number[::-1])

"""
String --> 
use '' or ""
sequence of character
Immutable
string variable --> store values in the String pool.
string pool presents inside the heap memory

string pool wont allow the duplicate values

if your creating multiple variables with same value
in string pool it will create one value and that value have multiple references

"""
name = "Guvi"
inst = "Guvi"
print(name)
print(name[0])
print(name[::-1])
print(name.lower())
print(name.isascii())
print(name.isdigit())
print(name.capitalize())
print("vidhya sagar".capitalize())
print("vidhya sagar".replace("a", "i"))
print("Vidhya Sagar".swapcase())

print("vidhya sagar".join("abcd"))
print("vidhya sagar".count("a"))
print("vidhya sagar"+"Guvi")
print(f"vidhya {455}")
#print("vidhya sagar"+45)

seq = "I am a automation tester"
print(len(seq))

print(len(seq.split(" ")))
date = "3/12/1995"
print(date.split("/"))

print(seq.split("a"))


# std = input("enter data")
# print(type(std))
# print(std.split(":"))

'''
Set 
----
mutable
it will follow the unorder collection of data
it wont allow the duplicates
One None values can stored
'''

actress = {"Aishwarya lakshmi", "Kalyani", "Madona"}
print(actress)
actress.add("9thara")
actress.add("9thara")
print(actress)
actress.add("3sha")
print(actress)
print(actress.pop())
print(actress)
#actress.remove("3sha")
actress.discard("3sha")
print(actress)



