#!/usr/bin/env python3
import os, time, datetime
import random
import requests

#mode = '[check]'
#mode = '[ on  ]'
mode = '[ off ]'

rand = random.randint(600,2200)
min = int(rand/60)
sec = rand%60

exe_time = (datetime.datetime.now() + datetime.timedelta(0,rand)).strftime("%Y-%m-%d %H:%M:%S")

time.sleep(rand)

url   = 'http://eadm.ncku.edu.tw/welldoc/ncku/iftwd/doSignIn.php'

check = {"Content-Type":"application/json","data":{"fn":"list","psnCode":"10502065","password":"10502065"}}

on    = {"Content-Type":"application/json","data":{"fn":"signIn","mtime":"A","psnCode":"10502065","password":"10502065",}}

off   = {"Content-Type":"application/json","data":{"fn":"signIn","mtime":"D","psnCode":"10502065","password":"10502065",}}

def clock_in(state):
    res = requests.post(url, json = state)
    #with open('/home/kk/Desktop/LOGS/clock_in.txt', "a") as file:
        #file.write(mode + '\t Execute at : '+ exe_time + '\n')
    #return print(res.text)

clock_in(off)

import smtplib

TO = 'kakinglin@gmail.com'
SUBJECT = 'INFORM MAIL'
TEXT = mode + '\t Execute at : '+ exe_time + '\n'

# Gmail Sign In
gmail_sender = 'kakinglin@gmail.com'
gmail_passwd = 'bpvfswzcogzdvtil'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

try:
    server.sendmail(gmail_sender, [TO], BODY)
    #print ('email sent')
except:
    print ('error sending mail')

server.quit()
