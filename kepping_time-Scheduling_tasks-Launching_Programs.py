# the time module
from datetime import datetime
import time
time.time()

def calcProd():
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))

time.ctime()
thisMoment = time.time()
time.ctime(thisMoment)

# Time.sleep() Function
import time
for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)
    
#Rounding Numbers
import time
now = time.time()
now
round(now, 2)
round(now, 4)
round(now)

#Project: Super Stopwatch
import time
#Display the program's instructions.
print("Press ENTER to begin. Afterward, press ENTER to 'click' the stopwatch. Press Ctrl-C to quit")
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time

except KeyboardInterrupt:
    # Handlle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
    

# The datetime Module
import datetime
datetime.datetime.now()
dt = datetime.datetime(2019,10,21,16,29,0)
dt.year, dt.month, dt.day

dt.hour, dt.minute, dt.second

# the timedelta Data Type
# represents a duration rather than a momment in time
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
delta.days, delta.seconds, delta.microseconds
delta.total_seconds()

dt = datetime.datetime.now()
dt
thousandDays = datetime.timedelta(days=1000)
dt + thousandDays

oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 300)
oct21st
oct21st - aboutThirtyYears

#pausing until a specific date
import datetimeimport time
halloween2022 = datetime.datetime(2022, 10, 31, 0, 0, 0)
while datetime.datetime.now() < halloween2022:
    time.sleep(1)
    
    
#Multithreading
import time, datetime

startTime = datetime.datetime(2029, 10, 31, 0, 0, 0)
while datetime.datetime.now() < startTime:
    time.sleep(1)
    
print('Program now starting on Halloween 2029')


import threading, time
print('Start of program.')

def takeANap():
    time.sleep(5)
    print('Wake up!')
    
threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program.')


#Launching Other Programs from Python
import subprocess
subprocess.Popen('C:\\Windows\\System32\\calc.exe')

#on ubuntu
import subprocess
subprocess.Popen('/snap/bin/gnome-calculator')


#import subprocess
paintProc = subprocess.Popen('C:\\Windows\\System32\\mspaint.exe')
paintProc.poll() == None
paintProc.wait() # Doesn't return until MS Paint closes

paintProc.poll()

