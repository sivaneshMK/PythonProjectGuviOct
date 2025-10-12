import string

name = "automation"

char_count = {}

# for char in name:
#
#     char_count[char]=0

# print(char_count)
#
# for key in char_count:
#     char_count[key]=name.count(key)
#
# print(char_count)

for char in name:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)



'''
check the password  is strong-->
    total len >= 8
    min 1 lower case
    min 1 upper case
    min 1 special character
    should not have any space

find words that start and end character are same Exa "Ananya", mom, malayalam, 

find the word is a palyndrom

reverse the word in a sentence
Ex:  I am a Automation Tester
o/p I ma a noitamotuA retseT

find the number from list whose sum of digit is even

Ex:  123
1+2+3 = 6

243
2+4+3 = 9

find number of vowels and consonants from the sentence

sort words in a sentence by length

Ex: "Python is an amazing programming language"
is an Python amazing language programming

sort dictionary by value
Ex: {"Ravi": 45, "Vidhya": 76, "Yamini": "03"}

{"Yamini": "03", "Ravi": 45, "Vidhya": 76}

'''


print(string.punctuation)

print("apply" > "banana")
print('a' > 'b')