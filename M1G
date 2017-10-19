#!/usr/bin/python3
import os, datetime, time, pathlib, re
import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

send_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

sender = 'kakinglin@gmail.com'
receivers = 'kakinglin@gmail.com'  

gmail_sender = 'kakinglin@gmail.com'
gmail_passwd = 'bpvfswzcogzdvtil'

#標題、內文
subject = '[M1G]'
content = 'Send time: ' + send_time

#创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header(sender, 'utf-8')
message['To'] =  Header(receivers, 'utf-8')
message['Subject'] = Header(subject, 'utf-8')
 
#邮件正文内容
message.attach(MIMEText(content, 'plain', 'utf-8'))
 
# 附件，目录下的 .dat 文件
filename = '00011771.dat'
attach = MIMEText(open(r'C:\Users\Roy\Desktop\test\\'+ filename, 'rb').read(), 'base64', 'utf-8')
attach["Content-Type"] = 'application/octet-stream'
attach["Content-Disposition"] = 'attachment; filename='+ filename
message.attach(attach)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)


try:
    server.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")

#-------------------------------------------------------------------------

path = 'C:/Users/Roy/Desktop/test/'
pathlib.Path(path).mkdir(parents=True, exist_ok=True)


url  = 'http://192.168.10.1/record/'
url_rebt = 'http://192.168.10.1/submit.php'
name = 'admin'
pwd  = 'password'
auth = HTTPBasicAuth(name,pwd)

res = requests.get(url,auth=auth)
soup = BeautifulSoup(res.text, 'lxml')
dats = soup.select('a')

for dat in range(1,len(dats)):
    dat = dats[dat].text[1:]
    print(url+dat,path+dat)
    #urlretrieve(url+dat, path+dat)

    
# 重新啟動
requests.post(url_rebt, data = {'REBOOT':'TRUE'})
