'''
while loop --> looping if statement
when:
    when your not sure about the end


while condition:
    statement
'''

value = 0

while value <=100:

    print(value)
    value+=1


# if user enter the even number the loop should get break

value = 2
while value%2 == 0:
    print(f"{value} is a even number")
    value = int(input("enterInput"))
else:
    print("odd number")



# if your giving a name it should print Hello + name until entering exit
# exit --> break


while True:
    name = input("enter name or exit: ")
    if name.lower()=="exit":
        break
    else:
        print("hello"+ name)

data = 1
while True:
    print(data)
    data+=1