import pyinputplus
"""
inputstr()
inputNum()
inputChoice()
inputMenu()
inputDatetime()
inputYesNo()
inputBool()
inputEmail()
inputEmail()
inputFilepath()
inputPassword()
"""

import pyinputplus as pyip
response = pyip.inputNum()

# The min, max, greaterThan, and lessThan keyword Arguements

response = pyip.inputNum('Enter num: ', min=4)
response = pyip.inputNum('Enter num: ', greaterThan=4)
response = pyip.inputNum('Enter num: ', min=4, lessThan=6)

#blank keyword arguement
response = pyip.inputNum(blank=True)

#The limit, timeout, and default keyword arguements
response = pyip.inputNum(limit=2)
response = pyip.inputNum(timeout=10)

response = pyip.inputNum(limit=2, default='N/A')

# The allowRegexes and blockRegexes keyword args
response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
 #---- This code will accept Roman numerals in addition to the usual numbers
response = pyip.inputNum(allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'])

response = pyip.inputNum(blockRegexes=[r'[02468]$'])
    #---this coed won't accept even numbers

response = pyip.inputNum(allowRegexes=[r'caterpillar', 'category'], blockRegexes=[r'cat'])
# try catastrophe

# Passing a custom validation function to inputCustom()
def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digit must add up to 10. not %s.' %(sum(numbersList)))
    return int(numbers)

response = pyip.inputCustom(addsUpToTen)

#try 123 1235 1234 


#PROJECT : HOW TO KEEP AN IDIOT BUSY FOR HOURS
"""pseudo code
    ask the user if they'd like to know how to keep an idiot busy for hours
    if answer is no: quit
    if answer is yes, got step 1
"""
import pyinputplus as pyip
while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)
    
    if response == 'no':
        break
    
print('Thank you. Have a nice day.')


#PROJECT:  MULTIPLICATION QUIZ

import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberofQuestions):
    #pick two random numbers:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    
    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    
    try:
        # Right answers are handled by allowRegexes
        # Wrong answers are handles by blockRegexes, with a custome message.
        pyinputplus.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)

    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
        
    else:
        # This block runs if no exceptions were raised in the try block
        print('Correct')
        correctAnswers += 1
        
        time.sleep(1)
        print('Score: %s / %s' % (correctAnswers, numberOfQuestions))


# TODO
# Sandwich maker
    """
    using inputMenu() for a bread type: wheat, white or sourdough
    using inputMenu() for a protein type: chicken, turkey, ham or tofu

    using inputYesNo() to ask if they want cheese
    if so, using inputMenu() to ask for cheese type: cheddar, Swiss, or mozzarella
    using inputYesNo() to ask is they want mayo, mustard, lettuce or tomato
    using inputInt() to ak how many sandwiches they want. Make sure this number is 1 or more

    """