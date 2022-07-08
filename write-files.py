from ctypes import windll
from pathlib import Path
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
from filename in myFiles:
    print(Path(r'C:\Users\Al', filename))
    
# The current working directory
from pathlib import Path
import os
Path.cwd()
os.chdir('C:\\Windows\\System32')
path.cwd()

Path.home()     #Home directory

#Checking path validity
winDir = Path('C:/Windows')
notExistsDir = Path('C:/This/Folder/Does/Not/Exist')
calcFile = Path('C:/Windows/System32/calc.exe')
winDir.exists()
winDir.is_dir()
notExistsDir.exists()
calcFile.is_file()
calcFile.is_dir()

dDrive = Path('D:/')
dDrive.exists()


#The File Reading/Writing Process
from pathlib import Path
p = Path('spam.txt')
p.write_text('hello, world!')

p.read_text()


# Opening files with the open() Function
helloFile = open(Path.home() / 'hello.txt')

helloFile = open('C:\\Users\\your_home_folder\\hello.txt')

helloFile = open('/Users/your_home_folder/hello.txt')


#Reading the Contemts of files
helloContent = helloFile.read()
helloContent

sonnetFile = open(Path.home() / 'sonnet29.txt')
sonnetFile.readlines()

#Writing to files
baconFile = open('bacon.txt', 'w')
baconFile.write('hello, world!\n')

baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')

baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)

# Saving Variables with the shelve Module
import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
type(shelfFile)

shelfFile['cats']
shelfFile.close()

shelfFile = shelve.open('mydata')
list(shelfFile.keys())

list(shelfFile.values())
shelfFile.close()


#Saving variables with the pprint.pformat() function
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')

fileObj.close()


#py progs generating py progs
import myCats
myCats.cats
myCats.cats[0]
myCats.cats[0]['name']

