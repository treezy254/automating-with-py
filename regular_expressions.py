import re
from email import message
# Without regular expressions

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))


print("-" * 20)


message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
    print('Done')

#-----------------------------------------------

# with regular expressions
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.') #mo = match objects
print('Phone number found: ' + mo.group())


#import ther regex module
# create a regex object with re.compile()
# pass the string to the search method
# call match object 

print("-" * 20)
#--------------------------------------------------

# grouping with paranthesis
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(1)
mo.group(2)
mo.group(0)
mo.group()
mo.groups()

areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

print("-" * 20)

#----------------------------------------------------

# matching multiple groups with the pipe

heroRegex = re.compile(r'Batman|Tine Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
mo1.group()

mo2 = heroRegex.search('Tina Fey and Batman')
mo2.group()

batRegex = re.compile(r"Bat(man|mobile|copter|bat)")
mo = batRegex.search('Batmobile lost a wheel')
mo.group()
mo.group(1)

print("-" * 20)

#--------------------------------------------------------

# optional matching with question mark


batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()


#----------------------------------------------------------

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
mo1.group()
mo2 = phoneRegex.search('My number is 555-4242')
mo2.group()

print("-" * 20)

#-----------------------------------------------------------

# Matching Zero or More with the Star

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()

mo2 = batRegex.search('The adventures of Batwoman')
mo2.group()

mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()

print("-" * 20)

#-------------------------------------------------------------
#matching One or more with the plus

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group()

mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo2.group()

mo3 = batRegex.search('The Adventures of Batman')
mo3 == None

print("-" * 20)

#-----------------------------------------------------------
# Matching Specific Repetitions with Braces

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo1.group()

mo2 = haRegex.search('Ha')
mo2 == None

print("-" * 20)

#-------------------------------------------------------------
# Greedy and Non-Greedy matching

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHa')
mo1.group()

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group()
print("-" * 20)

#--------------------------------------------------------------
# The findall() method

#search
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
mo.group()

#findall without groups
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')# has no groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')

#findall with groups
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')# has groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')

print("-" * 20)

#------------------------------------------------------------
# Character classes

#\d - any numeric digit from 0 - 9
#\D - any charcter that is not a digit from 0 to 9
#\w - any letter, nueric digit, or the underscore charcter. (Think of this as matching "word" characters)
#\W - Any charcater that is not a letter, numeric digit or the underscore charchter
#\s - Any space, tab or newline charchter. (matching space characters)
#\S - Any charcter that is not a space, tab or newline

# you can use the [a-zA-Z] charchter class or [0-5] -- dig deeper

xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 mainds, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

print("-" * 20)

#-----------------------------------------------------------
# Making your own character classes

vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')

# inside the square bracket, you don't need to escape the .,*,?,or() characters with a preceding backslash
# by placing a caret charachter (^) just after the character class's opening bracket, you can make a negative character class

consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantRegex.findall('RoboCop eats baby foof. BABY FOOD')

print("-" * 20)

#------------------------------------------------------------
# The Caret and Dollar Sign Charachters

# you can put a dollar sign at the end of the regex to indicate the string must end with this regex pattern

beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search("Hello World!")
beginsWithHello.search('He said hello.') == None

endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')
endsWithNumber.search('Your number is forty two.') == None

wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')
wholeStringIsNum.search('12345safaf67890') == None
wholeStringIsNum.search('12 34567890') == None

print("-" * 20)

#-------------------------------------------------------------

# The Wildcard Character

# matches any character except for a newline
atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')

# dor-star - greedy mode
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Samuel')
mo.group(1)
mo.group(2)

# dot-star-questionmark - non-greedy
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
mo.group()

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
mo.group()

print("-" * 20)

# Matching Newlines with the Dot Character

noNewlineREgex = re.compile(',*')
noNewlineREgex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group()

newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()





