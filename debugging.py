# Raising Exceptions
#sybtax
raise Exception('This is the error message')

#example
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise E('Symbol must be a single character string')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + ('' *(width - 2)) + symbol)
    print(symbol * width)
    
for sym, w, h in (('*',4,4), ('0',20,5), ('x',1,3),('ZZ',3,3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: ' +str(err))
        
        
# Getting the Traceback as a String
def spam():
    bacon()
    
def bacon():
    raise Exception('This is the error message.')

spam()

#<--- Instead of crashing my prog when the exception occurs, I can write the traceback info in a text-file and keep my programming running
from asyncio.log import logger
from distutils.debug import DEBUG
from distutils.log import ERROR, INFO
import logging
from re import I
import traceback
from tracemalloc import stop
try:
    raise Exception('This is the error message.')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')
    
# Assertions
#<-- contains, assert keyword, condition, comma and a string to display when !condition
ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
ages
# assert

ages.reverse()
ages
assert ages[0] <= ages[-1]


# Using an Assertion in a Traffic Light Simulation
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
            
switchLights(market_2nd)

assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight) 
    
    
    
# Logging
# USing the logging module
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging .debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))  
    total = 1
    for i in range(n + 1):
        total *= i 
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' %(n))
    return total

print(factorial(5))
logging.debug('End of program')

# Logging levels
"""
DEBUG       - logging.debug()
INFO        - logging.info()
WARNING     - logging.warning()    
ERROR       - logging.error()
CRITICAL    - logging.critical()
"""

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('an error message is about to be logged.')
logging.error('An error has ocured.')
logging.critical('The program is unable to recover!')

# Diabling Logging
import logging
logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.critical('Critical error! Critical error!')
logging.disable(logging.CRITICAL)
logging.critical('Critical error! Critical error!')
logging.error('Error! Error!')

# Logging to a File

import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


#Mu's Debugger
"""
    Continue - causes program to execute ni=ormally until it terminates or reaches a breakpoint
    Step In - cause the debugger to execute the next line of code and then pause again
    Step Over - executes the next line of code
    Step Out - causes the debigger to execute lines of code at full speed until it returns from the current function
    Stop - stops debugging entirely and doest bother with the rest of the code
    
"""

# Practice: DEbugging Coin Toss
import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
        
#OBJECTIVE: debug this game