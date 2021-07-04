list = []
n = int(input('How many numbers: '))
for i in range(n):
    numbers = int(input('Enter numbre'))
    list.append(numbers)
print("Sum of elements in given list is :", sum(list))