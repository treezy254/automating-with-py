# Projet: Phone number and Email Address Extractor

# Pseudo code

# . Get the text off the clipboard.
# 2. Find all phone numbers and email addresses in the text.
# 3. Paste them onto the clipboard.
# Now you can start thinking about how this might work in code. The 
# code will need to do the following:
# 1. Use the pyperclip module to copy and paste strings.
# 2. Create two regexes, one for matching phone numbers and the other 
# for matching email addresses.
# 3. Find all matches, not just the first match, of both regexes.
# 4. Neatly format the matched strings into a single string to paste.
# 5. Display some kind of message if no matches were found in the text.

# step 1: Create a regex for Phone Numbers

#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard

import pyperclip, re

phoneRegex = re.compile(r'''(
    \d{3}|\(\d{3}\))? # area code
 (\s|-|\.)? # separator
 (\d{3}) # first 3 digits
 (\s|-|\.) # separator
 (\d{4}) # last 4 digits
 (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
 )''', re.VERBOSE)


emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       #username
    @                   @ symbol
    [a-zA-Z0-9.-]+      # domain name
    (\.[a-zA-Z{2,4}])          # dot somrthing
)''', re.VERBOSE)

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
    
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
    