#Contolling mouse movement
import pyautogui
wh = pyautogui.size() #obtain the screen resolution
wh


#Moving the mouse
import pyautogui
for i in range(10):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)
    

#Getting the mouse position
pyautogui.position() # Get current mouse position
point(x=311, y=622)
pyautogui.position()
p = pyautogui.position()
p

p[0]
p.x

#Controlling Mouse Interaction
#Clicking the mouse

import pyautogui
pyautogui.click(10, 5)

#Dragging the mouse
import pyautogui, time
time.sleep(5)
pyautogui.click()   #click to make window active
distance = 300
change = 20
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.2)   # Move right
    distance = distance - change
    pyautogui.drag(0, distance, duration=0.2)   # Move down
    pyautogui.drag(-distance, 0, duration=0.2)  # Move left
    distance = distance - change
    pyautogui.drag(0, -distance, duration=0.2)  # Move up


# Scrolling the Mouse
pyautogui.scroll(200)


#Planning Mouse Movements
# Working with the screen
# Getting a screenshot
import pyautogui
im = pyautogui.screenshot()

#Analyzing the Screenshot
import pyautogui
pyautogui.pixel((0, 0))

pyautogui.pixel((50, 200))

pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))


#Image Recognition
import pyautogui
b = pyautogui.locateOnScreen('submit.png')
b
b[0]
b.left



# Getting window information
#Obtaining active window
import pyautogui
fw = pyautogui.getActiveWindow()
fw

str(fw)
fw.title
fw.size
fw.left, fw.top, fw.right, fw.bottom
fw.topleft
fw.area
pyautogui.click(fw.left + 10, fw.top + 20)


#Other methods
pyautogui.getAllWindows()
pyautogui.getWindowsAt(x, y)
pyautogui.getActiveWindowTitle(title)
pyautogui.getActiveWindow()

#Manipulating Windows
import pyautogui
fw = pyautogui.getActiveWindow()
fw.width    #gets the current width of the window
fw.topleft  # Gets the current position of the window
fw.width = 1000     # Resizes the width
fw.topleft = (800, 400) # Moves the window

fw.isMaximized
fw.isMinimized
fw.isActive
fw.maximize()
fw.restore()    # Undoes a minimize/maximize action
fw.minimize()
import time
# wait 5 seconds while you activate a different window
time.sleep(5); fw.activate()
fw.close()  # This will close the window you're typing in




# Controlling the Keyboard

# sending a string from the keyboard
pyautogui.click(100, 200); pyautogui.write('Hello, world!')

#Key Names
pyautogui.write(['a', 'b', 'left', 'left', 'X', 'Y'])

#Pressing and Releasing the Keyboard
pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')

# Hotkey combinations
pyautogui.keyDown('ctrl')
pyautogui.keyDown('c')
pyautogui.keyUp('c')
pyautogui.keyUp('ctrl')         #control copy


#Setting Up GUI Automation Scripts
"""
    Use the same screen resolution each time you run the script so that the 
position of windows doesn’t change.
•	 The application window that your script clicks should be maximized 
so that its buttons and menus are in the same place each time you run 
the script.
Controlling the Keyboard and Mouse with GUI Automation 493
•	 Add generous pauses while waiting for content to load; you don’t want 
your script to begin clicking before the application is ready.
•	 Use locateOnScreen() to find buttons and menus to click, rather than 
relying on XY coordinates. If your script can’t find the thing it needs 
to click, stop the program rather than let it continue blindly clicking.
•	 Use getWindowsWithTitle() to ensure that the application window you 
think your script is clicking on exists, and use the activate() method 
to put that window in the foreground.
•	 Use the logging module from Chapter 11 to keep a log file of what 
your script has done. This way, if you have to stop your script halfway 
through a process, you can change it to pick up from where it left off.
•	 Add as many checks as you can to your script. Think about how it could 
fail if an unexpected pop-up window appears or if your computer loses 
its internet connection. 
•	 You may want to supervise the script when it first begins to ensure that 
it’s working correctly
"""


"""You might also want to put a pause at the start of your script so the user 
can set up the window the script will click on. PyAutoGUI has a sleep() function that acts identically to time.sleep() (it just frees you from having to also 
add import time to your scripts). There is also a countdown() function that 
prints numbers counting down to give the user a visual indication that the 
script will continue soon. Enter the following into the interactive shell:"""

import pyautogui
pyautogui.sleep(3)
pyautogui.countdown(10)

print('Starting in ', end=''); pyautogui.countdown(3)
    