import random

responses = []
question = 0
number1 = 0
number2 = 0
answer = 0

while question != 10:
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
  
    print(str(number1) + " * " + str(number2) + " = ?")
    answer = int(input("What is the answer? "))
  
    if (answer == number1 * number2):
        responses.append(1)
        print("Correct!")
    else:
        responses.append(0)
        print("Incorrect!")
    
    question+=1
    
right = 0
wrong = 0
for entry in responses:
    if entry == 1:
        right += 1
    else:
        wrong += 1

print("You got " + str(right) + " questions correct!")
print("You got " + str(wrong) + " questions incorrect!")
