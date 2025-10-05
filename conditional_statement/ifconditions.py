

age = int(input("Enter age: ")) # type casting

if age >= 18: #true
    print("your eligible to vote")
else:
    print("your not eligible to vote")

if age%2==0:
    print("even Number")
else:
    print("Odd number")

alpha = input("Enter any character between A-Z: ")

# Vowels ---> aeiou
# consonant --> bcdfghjklmnpqrstvwxyz

if (alpha == 'a' or alpha=='e' or alpha=='i' or
        alpha=='o' or alpha=='u'):
    print("Vowel")
else:
    print("consonant")

vowels = 'aeiou'

if alpha.lower() in vowels:

       print(alpha+" is a vowel")
else:
    print(alpha+" is consonant")

'''
91-100 --> S Grade    
81-90 --> A Grade    
71-80 --> B Grade     
61-70 --> C Grade     
51-60 --> D Grade    
45 -50 --> E Grade   
0- 44 --> U Grade    

if else if

'''

mark = int(input("enter std mark: "))

if mark >=91 and mark <=100:
    print("S Grade")
elif 81 <= mark <= 90:
    print("A Grade")
elif 71 <= mark <= 80:
    print("B Grade")
elif 61 <= mark <= 70:
    print("C Grade")
elif 51 <= mark <= 60:
    print("D Grade")
elif 45 <= mark <= 50:
    print("E Grade")
elif 0 <= mark <= 44:
    print("U Grade")
else:
    print("invalid mark")

'''
1 DAY - 6MONTH --> INFANT
>6MONTH - 2YERS --> TODDLER
>2YERS - 4 YEARS --> CHILD
>4YERS - 12 YERS --> KID
>12 YERS -19 YERS --> TEEN
>19 YERS - 59 YERS --> ADULT
>59 YERS --> OLD



'''