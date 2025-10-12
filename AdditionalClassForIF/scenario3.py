
numbers = [5, 3, 4, 7, 9]
# numbers.sort()
print(numbers)

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] < numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print(numbers)


