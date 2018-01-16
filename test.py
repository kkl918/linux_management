#!/usr/bin/python3
import os, smtplib, ftplib, datetime, time, pathlib, re, requests, sys
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from requests.auth import HTTPBasicAuth
from ftplib import FTP

#import linebot
#-----------------------------------------------------------------------------------

# Create a dir on desktop for receive DATA
data_path = '/home/kk/Desktop/DATA/'
pathlib.Path(data_path).mkdir(parents=True, exist_ok=True)


# 依次序為[主機IP,使用者帳號,使用者密碼,FTP伺服器檔案路徑(FTP須先建立資料夾)]
ftp_ip  = '60.249.2.146'
ftp_usr = 'TBYT00'
ftp_pwd = 'TBYT0932867611'
ftp_cwd = '/homes/m1g_test'

# line機器人所要傳送的訊息
line_msg = 'M1G get data'

#-----------------------------------------------------------------------------------

url_submit = 'http://192.168.10.1/submit.php'

def m1g_test():
    nowtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    url  = 'http://192.168.10.1/record/'
    name = 'admin'
    pwd  = 'password'
    auth = HTTPBasicAuth(name,pwd)

    res = requests.get(url,auth=auth)
    soup = BeautifulSoup(res.text, 'lxml')

    dats = soup.select('a')
    for dat in range(1,len(dats)):
        dat = dats[dat].text[1:]
        print(dat)

m1g_test()
