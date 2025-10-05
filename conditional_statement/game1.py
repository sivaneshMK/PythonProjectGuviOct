'''

user - computer

rock - scissor  --> ur win
paper - rock  --> ur win
scissor - paper --> ur win

'''
import random

user = input("Enter  your choice: ")
# choices = {"rock", "paper", "scissor"}
# print(f"Choices {choices}")
# computer = choices.pop()
computer = random.choice(["rock", "paper", "scissor"])

print("Computer: "+computer)
if ((user =="rock" and computer == "scissor") or
    (user=="paper" and computer=="rock") or
    (user=="scissor" and computer=="paper")):

    print("user win")
elif computer==user:
    print("draw match")

else:
    print("Computer Win")