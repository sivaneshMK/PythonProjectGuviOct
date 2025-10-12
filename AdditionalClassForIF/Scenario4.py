# sum of digits

'''
a = 65
a%10 = 5

a//10 = 6


'''

def handle_number(number):
    def sum_digits(number):
        total = 0
        while number>0:

            digit = number % 10
            total += digit
            number //= 10

        return total
    return sum_digits(number)

# print(sum_digits(948))
#
# print(sum_digits(948839393))


print(handle_number(653))


def calculator(*values):

    def add(add_value):
        total =0
        for i in add_value:
            total+=i
        return total

    def mul(mul_value):
        total =1
        for i in mul_value:
            total*=i
        return total

    return add(values), mul(values)
sum, mul = calculator(1, 2,3,4, 5, 6,7,9, 1, 93, 7383)
print(sum)
print(mul)

def ex():
    return 66, 88

print(ex())


value = {2:"v", 4:"x"}

a, b = value

print(a)
print(b)

name = "Vidhya"

a, b, c, d,e, f= name

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)