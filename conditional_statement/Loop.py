import random

for i in range(1, 109):

    print(f"{i}: Sri rama jayam")

for i in range(1, 100):
    print(i)

for i in range(2, 101, 2):
    print(i)

for i in range(1, 101, 2):
    print(i)

# count number of vowels in the name
vowel_count =0
name = "karthic venkatachalam"
for i in range(len(name)):
    if name[i] in 'aeiouAEIOU':
        print(name[i]+" is vowel")
        vowel_count = vowel_count+1 # vowel_count += 1
    else:
        print(name[i]+ " is consonant")


print(vowel_count)
#karthic venkatachalam
reversed_name = ""
# for each loop
for i in name:
    reversed_name = i + reversed_name

print(reversed_name)

character = {}

for ch in name:
    character[ch] = 0
print(character)

for key in character:
    count = name.count(key)
    character[key] = count
print(character)

#
# for i in range(100):
#         number = random.randrange(1,1000)
#         user = int(input("guess the Number: "))
#         if number == user:
#             print("ho ho hooo you have found the number")
#             break
#         else:
#             print(f"oh oh number is {number}")

'''
*
* *
* * *
* * * *
* * * * *

'''

for r in range(1,6):
    for c in range(r):
        print("* ", end="")

        for d in range(r):
            print(d, end="")
    print()


abc = "sivanesh"

jumb = "".join(random.sample(abc, len(abc)))
print(jumb)