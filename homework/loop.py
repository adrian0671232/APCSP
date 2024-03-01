import random

numbers = []
evens = 0
odds = 0
sum = 0
minimum = 0
maximum = 0

for i in range(0, 100):
    numbers.append(random.randrange(0, 100))

for entry in numbers:
    if entry % 2 == 0:
        evens += 1
    else:
        odds += 1
    sum += i
    
sort = sorted(numbers)
minimum = sort[0]
maximum = sort[len(numbers) - 1]

print(numbers)
print("There are " + str(evens) + " even numbers.")
print("There are " + str(odds) + " odd numbers.")
print("The minimum number is " + str(minimum))
print("The maximum number is " + str(maximum))
print("The sum of all the values is " + str(sum))
