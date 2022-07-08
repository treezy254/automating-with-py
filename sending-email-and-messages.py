# Sending and recieving email with the Gmail API
from email import message
from xmlrpc.client import Server
import ezgmail, os
os.chdir(r'C:\path\to\credentials_json_file')
ezgmail.init()


# Sending Mail to a Gmail Account
ezgmail.send('recipient@example.com' 'Subject line', 'Body of the email', ['attachment1.jpg', 'attachment2.mp3', cc='friend@example.com', bcc="otherfriend@example.com,someoneelse@example.com"])

ezgmail.EMAIL_ADDRESS

#  Reading Mail from a Gmail account
import ezgmail
unreadThreads = ezgmail.unread() # list of GmailThread objects
ezgmail.summary(unreadThreads)

len(unreadThreads)
str(unreadThreads[0])

len(unreadThreads[0].messages)

str(unreadThreads[0].messages[0])

unreadThreads[0].messages[0].subject

unreadThreads[0].messages[0].body

unreadThreads[0].messages[0].timestamp # .recipient .sender etc

recentThreads = ezgmail.recent()
len(recentThreads)

recentThreads = ezgmail.recent(maxResults=100)
len(recentThreads)

# Searching Mail from a Gmail Account
resultThreads = ezgmail.search('RoboCop')
len(resultThreads)

ezgmail.summary(resultThreads)

# downloading Attachments from a Gmail Account
import ezgmail
threads = ezgmail.search('vaccation photos')
threads[0].messages[0].attachments

threads[0].messages[0].downloadAttachment('tulips.jpg')
threads[0].messages[0].downloadAllAttachments(downloadFolder="vacation2019")

#SMTP
# Sending Email - example with placeholders
import smtplib
smtpObj = smtplib.SMTP('smtp.example.com' 587)
smtpObj.ehlo()

smtpObj.starttls()

smtpObj.login('bob@example.com', 'password')
smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
smtpObj.quit()

#Connecting to an SMTP Server
smtpObj = smtplib.SMTP('smtp.example.com', 587)
type(smtpObj)
smtpObj = smtplib.SMTP_SSL('smtp.example.com', 465)

# Sending the SMTP "Hello" Message
smtpObj.ehlo()

# Starting TLS Encryption
smtpObj.starttls()

# Logging in to the SMTP Server
smtpObj.login('my_email_address@example.com', 'password')

#Sending an Email
smtpObj.sendmail('my_email_address@example.com', 'recipient@example.com', 'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')

# Disconnecting from the SMTP Server
smtpObj.quit()


#IMAP
# Retrieving and Deleting Emails with IMAP
import imapclient
imapObj = imapclient.IMAPClient('imap.example.com', ssl=True)
imapObj.login('my_email_address@example.com', 'MY_SECRET_PASSWORD')

imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['SINCE os-Jul-2019'])
UIDs

rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])
import pyzmail
message = pyzmail.Pyzmail.PyzMessage.factory(rawMessages[40041][b'BODY[]'])
message.get_subject()
    #   .get_addresses('from')
    #   .get_addresses("to")
    #   .get_addresses('cc')
    #                   ('bcc')
message.text_part != None

message.text_part.get_payload().decode(message.text_part.charset)
message.html_part != None
message.html_part.get_payload().decode(message.text_aprt.charset)
message.html_part != None
message.html_part.get_payload().decode(message.html_part.charset)
imapObj.logout()


# Connecting to an IMAP Server
import imapclient
imapObj = imapclient.IMAPClient('imap.example.com', ssl=True)

#Logging in to the IMAP Server
imapObj.login('my_email_address@example.com', 'my_secret_password')

#seaching for email
#--selecting folders
import pprint
pprint.pprint(imapObj.list_folders())

imapObj.select_folder('INBOX', readonly=True)

#--performing the Search
UIDs = imapObj.search(['SINCE 05-jul-2019'])
UIDs

#--size Limits
import imaplib
imaplib._MAXLINE = 1000000

# Fetching an Email and amrking it as read
rawMessages = imapObj.fetrch(UIDs, ['BODY[]'])
import pprint
pprint.pprint(rawMessages)

#Gettting Email Addresses from a Raw Message
import pyzmail
message = pyzmail.PyzMessage.factory(rawMessages[40041][b'BODY[]'])
message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('cc')
message.get_addresses('bcc')

# Getting the Body from a raw message
message.text_part != None
message.text_part.get_payload().decode(message.text_part.charset)
message.html_part != None
message.html_part.get_payload().decode(message.html_part.charset)


# Deleting Emails
imapObj.select_folder('INBOX', readonly=False)
UIDs = imapObj.search(['ON 09-Jul-2019'])
UIDs

imapObj.delete_messages(UIDs)
imapObj.expunge()

# Disconnecting from the IMAP Server
imapObj.logout()

# --------------------------------

#SENDING TEXT MESSAGES with TWILIO
from twilio.rest import Client
accountSID = 'ACxxxxxxxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
twilioCli = Client(accountSID, authToken)
myTwilioNumber = '+2324242'
myCellphone = '+12324223'
message = twilioCli.messages.create(body='Mr. Watson - Come here - I want to see you.', from_=myTwilioNumber, to=myCellphone)


#PROJECT : "JUST TEXT ME" Module
# textMyself.py - Defines the textmyself() function that texts a message
#passed to it as a string

# present values:
accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxxxxxxx'
myNumber = "+1323424535"
twilioNumber = '+13242323'

from twilio.rest import Client

def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)
    
# whenever I want one of my programs to text me, I just add the following
import textmyself
textmyself.textmyself('The boring task is finished')

