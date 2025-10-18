import re

name = " automation testing python, python"

pattern = r"python"

match = re.match(pattern, name)

if match:
    print("found", match.group())
else:
    print("not found")

print(re.search(pattern=pattern, string=name))

print(re.findall(pattern, name))


words = "cat mat rat hat dog bat chat 123at at383  at"



patt = r"\w+at"

print(re.findall(patt, words))
email = "sivaneshkirubanandham03@gmail.com"
patt= r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

print(re.findall(patt, email))


'''
/w --> word characters
/s --> space
. --> any character except new line
^ --> start of string
$ --> end of the string
+ --> one or more
* --> zero or more
{n, m} --> between n and m times
/d --> digit    


'''



