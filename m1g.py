#!/usr/bin/python3
import os, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import datetime, time, pathlib, re, requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from requests.auth import HTTPBasicAuth
#-----------------------------------------------------------------------------
#標題、內文
subject = 'M1G test in NCKU'
content = 'content'

data_path = r'/home/kk/Desktop/DATA/'
pathlib.Path(data_path).mkdir(parents=True, exist_ok=True)
#-----------------------------------------------------------------------------

url_submit = 'http://192.168.10.1/submit.php'
data     = 'REBOOT=TRUE'

url  = 'http://192.168.10.1/record/'
name = 'admin'
pwd  = 'password'
auth = HTTPBasicAuth(name,pwd)

res = requests.get(url,auth=auth)
soup = BeautifulSoup(res.text, 'lxml')
dats = soup.select('a')

#-----------------------------------------------------------------------------

sender = 'kakinglin@gmail.com'
receivers = 'survey0669@gmail.com'  

gmail_sender = 'kakinglin@gmail.com'
gmail_passwd = 'bpvfswzcogzdvtil'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)

#创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("kk", 'utf-8')
message['To'] =  Header("Chen", 'utf-8')
message['Subject'] = Header(subject, 'utf-8')
 
#邮件正文内容
message.attach(MIMEText(content, 'plain', 'utf-8'))
#-----------------------------------------------------------------------------

def m1g_getData():
	for dat in range(1,len(dats)):
		dat = dats[dat].text[1:]
		if dat in os.listdir(data_path):
			pass
		else:
			print(url+dat,data_path+dat)
			urlretrieve(url+dat, data_path+dat)
			attach = MIMEText(open(data_path + dat, 'rb').read(), 'base64', 'utf-8')
			attach["Content-Type"] = 'application/octet-stream'
			attach["Content-Disposition"] = 'attachment; filename='+ dat
			message.attach(attach)
			try:
				server.sendmail(sender, receivers, message.as_string())
				print ("邮件发送成功")
			except smtplib.SMTPException:
				print ("Error: 无法发送邮件")

def m1g_reboot():
	requests.post(url_submit, data = {'REBOOT':'TRUE'})
	
def m1g_stop():
	requests.post(url_submit, data = {'CMD':'DEVICE.RECORD.STOPRECORD'})
def m1g_start():
	requests.post(url_submit, data = {'CMD':'DEVICE.RECORD.STARTRECORD'})
#-----------------------------------------------------------------------------

m1g_getData()
#m1g_stop()
#time.sleep(1)
m1g_start()
