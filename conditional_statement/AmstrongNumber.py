
input=input("Enter number") # 153
power = len(input) # 3
total = 0
for d in input:

    #total += int(d)**power
    total = total + int(d)**power


if total == int(input):
    print(input+"Armstrong number")
else:
    print("Not a armstrong ")


