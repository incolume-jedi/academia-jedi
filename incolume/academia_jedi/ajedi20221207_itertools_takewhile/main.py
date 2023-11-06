from itertools import takewhile

numbers = [1, 2, 3, -1, 3, 2, 1]

for number in numbers:
    if number <= 0:
        break
    print(number)

print()
items = takewhile(lambda x: x >= 0, numbers)
for item in items:
    print(item)
