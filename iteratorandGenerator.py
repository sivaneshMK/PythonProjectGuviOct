
'''

An iterator is an object that allows you to iterate(loop) through a sequence one at time

__iter__() --> return iterator object
__next__() --> return the next item in the sequence

iterator will consume memory space
it will store all the values and process everything togather




'''


number= [83, 8393, 8393, 89, 893, 989]
itr = iter(number)
print(iter(number))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))


'''
Generator
------------
A Generator is a special method that automatically creates an iterator

instead of return we have to use yield keyword . proceed values one at a time

when the funtion is called it doesn't run completely
it pauses at yield remembers its state and resume from next time'

'''

def count(n):
    i=1
    while i<=n:
        yield i
        i +=1

coun = count(10)

#
# for n in coun:
#     print(n)
#

print(next(coun))
print(next(coun))
print(next(coun))
print(next(coun))


def normal():
    i=0
    while True:
        yield i
        i+=1
num = normal()
print(num)
print(next(num))
print(next(num))
print(next(num))


def so():
    yield 1
    yield 2
    yield 3

s = so()
print(s)
print(next(s))
print(next(s))
print(next(s))