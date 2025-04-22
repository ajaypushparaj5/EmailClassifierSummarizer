import imaplib as imap  
import email
import os
from dotenv import load_dotenv
load_dotenv()
mail=imap.IMAP4_SSL('imap.gmail.com')
user=os.getenv('useremail')
passw=os.getenv('password')
print(user)
print(passw)
mail.login(user,passw)
mail.select('inbox')
status,messages=mail.search(None,'ALL')
emails=messages[0].split()
emailid=emails[-1]
status,msgdata=mail.fetch(emailid,'(RFC822)')
msg=email.message_from_bytes(msgdata[0][1])
subject=msg['subject']
fromm=msg['from']
date=msg['date']
print(" from: ",fromm,' Subject: ',subject,' Date: ',date)
