# All code written by Steven Claros

import random

# Here we set the options and possibilities for the 3 things we will roll (coin flip, dice roll, spinner)
coinOpt = random.randint(0, 1)
# coinOpt is either 0 or 1 because a coinflip is a 50/50 and just 2 options (Heads or Tails)
dice = random.randint(0, 6)

spinnerList = ['red', 'yellow', 'blue', 'green']
spinner = spinnerList[random.randint(0, len(spinnerList) - 1)]
# This allows us to choose a random color from our spinnerList

coin = 'Heads' if coinOpt == 0 else 'Tails'
# this gives the coins variable the name

# Here we just print text and input
print('''
****WELCOME****
This is our game of chance.
Let's see if you won...

''')

print('What is your guess on the dice roll?')
diceGuess = int(input())
print('What is your guess on the coin flip, Heads (H) or Tails (T)')
coinGuess = input()
print('What is your guess on the spinner, red (r), green (g), blue (b), or yellow (y)?')
spinnerGuess = input()

# Here we tell the user what was rolled/spun/flipped
print('You rolled a ' + str(dice))
print('You flipped ' + coin)
print('You spun ' + spinner)

# By turning coinGuess into an int we can check if it is heads or tails by using ==
coinGuess = 0 if 'H' in coinGuess else 1 if coinGuess == 1 else 2

coinResult = coinOpt == coinGuess
diceResult = dice == diceGuess
spinnerResult = spinnerGuess == spinner[0]

# I decided to make the result a list, this way we can add result messages optimally instead of multiple if statements
resultMessage = ['You got']
message = ''

if coinResult:
    resultMessage.append(' and the coin flip')
if diceResult:
    resultMessage.append(' and the dice roll')
if spinnerResult:
    resultMessage.append(' and the spin')

# The length of the list will always be more than 1 if something was appended
if len(resultMessage) > 1:
    # This just helps with formatting the message
    resultMessage[1] = resultMessage[1][4:]
    resultMessage.append(' correct!')
    for result in resultMessage:
        message = message + result
    print(message)
else:
    resultMessage = 'Sorry, you somehow managed to get NOTHING correct.'
    print(resultMessage)
