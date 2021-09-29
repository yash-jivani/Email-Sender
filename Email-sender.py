
import smtplib
from email.message import EmailMessage
import time
import re
import os

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def check(email):
    if(re.search(regex, email)):
        pass
    else:
        print("Invalid Email")
        exit()

path1 = os.getcwd()
userTo = input('Send To : ')
check(userTo)
userSub = input("Email's Subject : ")
userFrom = input('From : ')

lines = int(input('How many lines you need to write your mail : '))
msg = EmailMessage()
msg['To'] = userTo
msg['Subject'] = userSub
msg['From'] = userFrom
print('strat writing your mail :: ')
while lines > 0:
    with open('mail-info.txt', 'a') as wf:
        data = input(f'{lines-1} lines left : ')
        wf.write(data+'\n')
    lines -= 1

with open('mail-info.txt') as rf:
    data = rf.read()
    msg.set_content(data)

print('''
############################################################################

https://myaccount.google.com/security

Sign in to your Google Admin console. ...
From the Admin console Home page, go to Security. ...
To apply the setting to everyone, leave the top organizational unit selected. ...
Select the setting for less secure apps: TURN IT ON !
Click Save.

#############################################################################

''')
time.sleep(1.5)
logASAddress = input('\nEnter Your Email address : ')
logASPswd = input('Enter Your Password : ')
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
try:
    server.login(logASAddress, logASPswd)
except:
    print('\n[-] Somthong went wrong !')
    print('[!] Plz read NOTES | Check your mail address and password !\n')
    os.remove(path1+'/mail-info.txt')
    exit()

try:
    server.send_message(msg)
except:
    print("[-] Somthing went wrong !")
    print('[!] Invaild email\n')
    exit()
finally:
    os.remove(path1+'/mail-info.txt')
    server.quit()
print('\n[+] Email send successfully !\n')
