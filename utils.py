import imaplib as imap  
import email
import os
mail=imap.IMAP4_SSL('imap.gmail.com')
useremail=os.getenv('useremail')
passwrd=os.getenv('password')

mail.login(useremail,passwrd)
mail.select('inbox')
status,messages=mail.search(NONE,'ALL')
emails=messages[0].split()
emailid=emails[-1]
status,msgdata=mail.fetch(emailid,'(RFC822)')
msg=email.message_from_bytes(msgdata[0][1])
subject=msg['subject']
fromm=msg['from']
date=msg['date']
print(" from: ",fromm,' Subject: ',subject,' Date: ',date)
