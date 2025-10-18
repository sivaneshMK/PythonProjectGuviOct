# def add(a, b):
#     return a+b

add = lambda x, y: x+y

print(add(3, 7))

number = [1, 2, 3, 4, 5, 6]

root = list(map(lambda x: x**2, number))
print(root)
print(map(lambda x: x**2, number))


z = [11, 22, 33, 44, 55]
w = [54, 5,2,2, 4, 7]
print(tuple(map(add, w, z)))

'''
The map is a function
it is used to apply a function to every item in an iterable(like list, tuple, ect).
it is return a map object(which you can covert to a list, tuple)


1. add 10 to all values in the list
2. convert all words into a lowercase
3. add all the digits in the number(sum of digits)

'''


std = ["karthic", "Vidhya", "paul", "Thavamani", "Amalarasi"]
Tamil=[84, 82, 73, 73, 89]
English = [84, 82, 73, 78, 87]
Maths = [73, 45, 73, 73, 89]
Science = [83, 82, 42, 83, 98]
History = [83, 82, 42, 83, 98]

total = list(map(lambda a, b, c, d, e: a+b+c+d+e, Tamil, English, Maths, Science, History))

print(total)

result = list(map(lambda st, t: f"{st }: {t}", std, total))
print(result)


def abc():
    print(add(4, 5))


def sub(a,b):
    value = lambda a, b: a - b
    return value(a, b)

print(sub(7, 4))