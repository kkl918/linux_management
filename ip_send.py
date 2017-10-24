#!/usr/bin/python
import smtplib, tome
from email.message import EmailMessage
from subprocess import check_output
def ip_send():
  ip = check_output(["hostname", "-I"]).decode()
  #print(ip)

  ifconfig = check_output(["ifconfig"]).decode()
  #print(ifconfig)

  TO = 'kakinglin@gmail.com'
  SUBJECT = 'About IP'
  TEXT = 'hostname -I:'+ ip + '\n' + ifconfig

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
      print ('email sent')
  except:
      print ('error sending mail')

  server.quit()

time.sleep(60)
ip_send()
time.sleep(60)
ip_send()
time.sleep(60)
ip_send()
time.sleep(60)
ip_send()
time.sleep(60)
ip_send()
time.sleep(60)
ip_send()
time.sleep(60)
ip_send()
time.sleep(60)
ip_send()
  
