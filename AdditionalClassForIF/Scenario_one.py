
'''
I have a sentence
"I am a automation tester"

Find the biggest word
second biggest word
'''

sen = "I am a automation  engineer in tester's"
words = sen.split() # ['I', 'am', 'a', 'automation', 'tester']

biggest_word = ""

for word in words:
    if len(word)>len(biggest_word):
        biggest_word = word

second_biggest = ""



for word in words:
    if len(word)<len(biggest_word) and len(word) >len(second_biggest):
        second_biggest = word


#second_biggest_words= [word for word in words if len(word)==len(second_biggest)]

second_biggest_words = []
for word in words:
    if len(word)== len(second_biggest):
        second_biggest_words.append(word)


print("second biggest words", second_biggest_words)
print("biggest word is "+biggest_word)
print("second biggest word "+ second_biggest)



sen = "I am a automation developer and a unit tester in capgimini sivaneshmk"
word = sen.split()

first_biggest_word = ""
second_biggest_word = ""
first_biggest_words = []
second_biggest_words = []

for word in word:
    if len(word) > len(first_biggest_word):
        second_biggest_word = first_biggest_word
        first_biggest_word = word
        first_biggest_words = [word]
    elif len(word) == len(first_biggest_word):
        first_biggest_words.append(word)
    elif len(word) > len(second_biggest_word):
        second_biggest_word = word
        second_biggest_words = [word]
    elif len(word) == len(second_biggest_word):
        second_biggest_words.append(word)

print("The first biggest word(s):", first_biggest_words)
print("The second biggest word(s):", second_biggest_words)


