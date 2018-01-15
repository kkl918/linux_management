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

def m1g_getData():
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
		if dat in os.listdir(data_path):
			pass
		else:
			print(url+dat,data_path+dat)	
			urlretrieve(url+dat, data_path+dat)
			print("Start transmission of FTP.")
			ftp = FTP(ftp_ip)
			ftp.login(ftp_usr, ftp_pwd)
			ftp.cwd(ftp_cwd)
			file_ = open('/home/kk/Desktop/DATA/'+ dat,'rb')
			#ftp.storbinary('STOR %s' % dat, file_)
			ftp.quit() 
			file_.close() 
			print("File transfered" + nowtime)
			
def m1g_reboot():
	requests.post(url_submit, data = {'REBOOT':'TRUE'})
	
def m1g_stop():
	requests.post(url_submit, data = {'CMD':'DEVICE.RECORD.STOPRECORD'})

def m1g_start():
	requests.post(url_submit, data = {'CMD':'DEVICE.RECORD.STARTRECORD'})

#-----------------------------------------------------------------------------

if __name__ == '__main__':
    #line = linebot.bot.single_text(line_msg) # 不必改動也勿改動
    
    if len(sys.argv) < 2:
        print('No argument')
        sys.exit()

    if sys.argv[1].startswith('--'):
        option = sys.argv[1][2:]
        if option == 'on':
            m1g_start() 
        elif option == 'off':
            m1g_stop()
            m1g_getData()
        elif option == 'reboot':
            m1g_reboot()
        else:
            print('[--on] [--off] [--reboot]')
            sys.exit()
    else:
        print('wrong type argv')
        sys.exit()

    # 以下為程序運行順序，依次序由上至下
    # -------------------------------------------------------
    #m1g_stop()      # M1G停止紀錄
    #time.sleep(10)  # 程序暫停10秒(可自定義秒數)
    #m1g_getData()   # #M1G抓取資料到主機並推送自遠端FTP站台
    #m1g_start()     # M1G開始紀錄
    #line()          # line機器人傳送訊息
    #mail_send()     # 寄送EMAIL(此版本無此功能，勿啟用會自造成錯誤)
    #m1g_reboot()    # M1G重開機
    # -------------------------------------------------------
    # END
