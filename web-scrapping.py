#Project: maplt,py with the webbrowser Module
import webbrowser

import pyperclip
webbrowser.open('https://inventwithpy.com/')

# What the program does
"""
    gets a street address from the command line arguements/clipboard
    Opens the web browser to the Google Maps page for the address
    ie:
        read the command line arguements from sys.argv
        read the clipboard contents
        call the webbrowser.open() function to open the web browser
"""

# Step1: Figure out the Url
# clipboard: <-- C:\> mapit 870 Valencia St, San Franscisco, CA 94110

#Step2: Handle the Command Line Arguements

import webbrowser, sys
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
    
#TODO: Get address for clipboard

else:
    address = pyperclip.paste()
    
webbrowser.open('https://www.google.com/maps/place/'+address)


# Downloading Files from the web with the requests Module
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
res.status_code == requests.code.ok
len(res.text)
print(res.text[:250])

#Checking for Errors
res = requests.get('https://incentwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
    

# Saving Downloaded Files to the Hard Drive
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomesAndJuliet.txt', 'wb')
for chunk in res.iter_content(1000000):
    playFile.write

#....
playFile.close()



#Creating a BeuatifulSoup Object from HTML
import requests, bs4
res = requests.get('https://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
type(noStarchSoup)

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
type(exampleSoup)


#Finding an Element with the select() Method

import bs4
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('#author')
type(elems)
len(elems)
type(elems[0])
str(elems[0])
elems[0].getText()
elems[0].attrs
pElems = exampleSoup.select('p')
str(pElems[0])
pElems[0].getText()
str(pElems[0])
pElems[0].getText()
str(pElems[1])
pElems[1].getText()
str(pElems[2])
pElems[2].getText()


#Getting Data from an Element's Attributes
import bs4
soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
spanElem = soup.select('span')[0]
str(spanElem)

spanElem.get('id')
spanElem.get('some_nonexistent_addr') == None
spanElem.attrs

#Controlling the browser with selenium Module

from selenium import webdriver
browser = webdriver.Firefox()
type(browser)

browser.get('https://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name(' cover-thumb')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
    
# clicking the page

linkElem = browser.find_element_by_link_text('Read Online for Free')
type(linkElem)
linkElem.click()

# filling out and submitting forms
userElem = browser.find_element_by_id('user_name')
userElem.send_keys('your_real_username_here')

passwordElem = browser.find_element_by_id('user_pass')
passwordElem.send_keys('Your_real_password_here')
passwordElem.submit()

# Sending Special Keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('https://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)    #Scrolls to bottom
htmlElem.send_keys(Keys.HOME)   # scrolls to top

# other methods
"""
       browser.back()       # Clicks the Back button
       browser.forward()    # Clicks the Forwars button
       browser.refresh()    # Clicks the Refersh/Reload button
       browser.quit()       # Clicks the Close Window button
"""

# more projects
"""
        commmand Line Emailer
        Image site Downloader
        2048
        Link Verification
        """

