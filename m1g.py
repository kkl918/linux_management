#!/usr/bin/python3
import os, smtplib, ftplib, datetime, time, pathlib, re, requests, sys, gzip, shutil
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from requests.auth import HTTPBasicAuth
from ftplib import FTP

import line_msg
#-----------------------------------------------------------------------------------

# Create a dir on desktop for receive DATA
data_path = '/home/kk/Desktop/DATA/'
data_gz_path = '/home/kk/Desktop/DATA_GZ/'
pathlib.Path(data_path).mkdir(parents=True, exist_ok=True)
pathlib.Path(data_gz_path).mkdir(parents=True, exist_ok=True)

# 次序為[主機IP,使用者帳號,使用者密碼,FTP伺服器檔案路徑(FTP須先建立資料夾)]
ftp_1 = ['140.116.89.125','azes','azes00','/azes_gz']
ftp_2 = ['60.249.2.146','TBYT00','TBYT0932867611','/homes/azes_gz']


# line要發送的訊息
msg2line = 'M1G in AZES :'


#-----------------------------------------------------------------------------------
url_submit = 'http://192.168.10.1/submit.php'

def m1g_getData(ftp_server):
    nowtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    url  = 'http://192.168.10.1/record/'
    name = 'admin'
    pwd  = 'password'
    auth = HTTPBasicAuth(name,pwd)

    res = requests.get(url,auth=auth)
    soup = BeautifulSoup(res.text, 'lxml')
    dats = soup.select('a')
    # 對要下載的檔案進行控制
    for dat in range(1,len(dats)-1):
        dat = dats[dat].text[1:]

        if dat in os.listdir(data_path):
            pass
        else:
            print('Start to download data.')
            urlretrieve(url+dat, data_path+dat)
            print(url+dat,data_path+dat + ' -> getDATA successed.')
            line_msg.bot().send_text(msg2line + ' get data to pi successed.')
'''
            ftp = FTP(ftp_server[0])
            ftp.login(ftp_server[1], ftp_server[2])
            ftp.cwd(ftp_server[3])
            file_ = open(data_path + dat,'rb')
            ftp.storbinary('STOR %s' % dat, file_)
            ftp.quit()
            file_.close() 
            print("File transfered " + nowtime)
'''    
def m1g_reboot():
    requests.post(url_submit, data = {'REBOOT':'TRUE'})
    print('Reboot M1G successed.')
    line_msg.bot().send_text(msg2line + ' Reboot M1G successed.')

def m1g_stop():
    requests.post(url_submit, data = {'CMD':'DEVICE.RECORD.STOPRECORD'})
    print('Stop M1G successed.' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    line_msg.bot().send_text(msg2line + ' Stop M1G successed.')

def m1g_start():
    requests.post(url_submit, data = {'CMD':'DEVICE.RECORD.STARTRECORD'})
    print('Start M1G successed.' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n')
    line_msg.bot().send_text(msg2line + ' Start M1G successed.')

def m1g_gz(src_path,dst_path):
    for file in os.listdir(src_path):
        if file + '.gz' not in os.listdir(dst_path):
            print('Start compres file : ' + file)
            with open(src_path + file, 'rb') as f_in, gzip.open(dst_path + file + '.gz', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

# for 陳南安 FTP
def m1g_ftp_unix(info, src_path):
    ftp = FTP(info[0])
    ftp.login(info[1], info[2])
    ftp.cwd(info[3])
    ftp_list = ftp.nlst(info[3])
    
    # 建立FTP內檔案清單
    ftp_unix =[]
    for file in ftp_list:
        ftp_unix.append(file[-15:])

    # 比對本地端以及遠端檔案內容
    for dat in os.listdir(src_path):

        if dat in ftp_unix:
            pass
        else:
            print('Start   transmission for : '+ dat)
            file2ftp = open(src_path + dat, 'rb')
            try:
                ftp.storbinary('STOR %s' % dat , file2ftp)
                print('Finish  transmission at ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                line_msg.bot().send_text(msg2line + ' sync M1G and FTP successed.')
            except:
                print('Transmission error.')
                line_msg.bot().send_text(msg2line + ' sync error.')
                ftp.quit()
                sys.exit()
    print('sync done.')

def m1g_ftp_win(info, src_path):
    ftp = FTP(info[0])
    ftp.login(info[1], info[2])
    ftp.cwd(info[3])
    ftp_list = ftp.nlst(info[3])
    
    # 建立FTP內檔案清單
    ftp_win =[]
    for file in ftp_list:
        ftp_win.append(file)
        
    # 比對本地端以及遠端檔案內容
    for dat in os.listdir(src_path):
        if dat in ftp_win:
            pass
        else:
            print('Start   transmission for : '+ dat)
            file2ftp = open(src_path + dat,'rb')
            try:
                  ftp.storbinary('STOR %s' % dat, file2ftp)
                  print('Finish  transmission at ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                  line_msg.bot().send_text(msg2line + ' sync M1G and FTP successed.')
            except:
              print('Transmission error.')
              line_msg.bot().send_text(msg2line + ' sync error.')
              ftp.quit()
              sys.exit()
    print('sync done.')   
   
def m1g_test():
    nowtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    url      = 'http://192.168.10.1/record/'
    url_down = 'http://192.168.10.1/download.php'
    url_stat = 'http://192.168.10.1/#ib-status/'
    name = 'admin'
    pwd  = 'password'
    auth = HTTPBasicAuth(name,pwd)

    res = requests.get(url_down,auth=auth)
    soup = BeautifulSoup(res.text, 'lxml')
    file_info = {}
    dats = soup.select('tr')
    for i in range(len(dats)):
        last_file = dats[len(dats)-1].text[:12]
    for dat in dats[1:]:
        for i in range(len(dat.text)-12):
            num = 0
            if dat.text[12+i] == 'M':
                file_info[dat.text[:12]] = dat.text[12:13+i]
            elif dat.text[12+i] == 'K':
                file_info[dat.text[:12]] = dat.text[12:13+i]
            elif dat.text[12+i] == 'B':
                file_info[dat.text[:12]] = dat.text[12:13+i]
            else:
                print('Test error.')
    for key in file_info.keys():
        print(key, file_info[key])
    
    size1 = file_info[last_file]
    print('Last file is : ' + last_file + ' ' +file_info[last_file])
    line_msg.bot().send_text(msg2line + 'Last file is : ' + last_file + ' ' +file_info[last_file])
    
    time.sleep(5)
    
    res = requests.get(url_down,auth=auth)
    soup = BeautifulSoup(res.text, 'lxml')
    dats = soup.select('tr')
    for i in range(len(dats)):
        last_file = dats[len(dats)-1].text[:12]
    for dat in dats[1:]:
        for i in range(len(dat.text)-12):
            num = 0
            if dat.text[12+i] == 'M':
                file_info[dat.text[:12]] = dat.text[12:13+i]
            elif dat.text[12+i] == 'K':
                file_info[dat.text[:12]] = dat.text[12:13+i]
    size2 = file_info[last_file]
    print('After 5 seconds : ' + last_file + ' ' +file_info[last_file])
    line_msg.bot().send_text(msg2line + 'After 5 seconds : ' + last_file + ' ' +file_info[last_file])
    if size2[:-1] > size1[:-1]:
        print('M1G is working well.' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        line_msg.bot().send_text(msg2line + 'M1G is working well.' + ' ' +datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
def m1g_line():
    # line機器人所要傳送的訊息
    line_id_an  = line_msg.bot.an_id
    line_id_ro  = line_msg.bot.root_id
    line_text = 'Line fuction test at ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line_msg.bot().send_text(msg2line + line_text)

#-----------------------------------------------------------------------------
if __name__ == '__main__':  
    if len(sys.argv) < 2:
        print('No argument')
        sys.exit()

    if sys.argv[1].startswith('--'):
        option = sys.argv[1][2:]
        if option == 'start':
            m1g_start()
            
        elif option == 'get':
            m1g_getData(ftp_2)
            
        elif option == 'stop':
            m1g_stop()
            
        elif option == 'reboot':
            m1g_reboot()
            
        elif option == 'ftp_unix':
            m1g_ftp_unix(ftp_2, data_gz_path)
            
        elif option == 'ftp_win':
            m1g_ftp_win(ftp_1, data_gz_path)
            
        elif option == 'test':
            m1g_test()
            
        elif option == 'line':
            m1g_line()
            
        elif option =='gz':
            m1g_gz(data_path,data_gz_path)
            
        else:
            print('try : [--start] [--stop] [--reboot] [--get] [--ftp_unix] [--test] [--line]')
            sys.exit()
    else:
        print('wrong type argv')
        sys.exit()

    '''
    # 以下為程序運行順序，依次序由上至下
    # -------------------------------------------------------
    #m1g_stop()      # M1G停止紀錄
    #m1g_getData()   # #M1G抓取資料到主機並推送自遠端FTP站台
    #time.sleep(300)  # 程序暫停10秒(可自定義秒數)
    #m1g_start()     # M1G開始紀錄
    #line()          # line機器人傳送訊息
    #mail_send()     # 寄送EMAIL(此版本無此功能，勿啟用會自造成錯誤)
    #m1g_reboot()    # M1G重開機
    # -------------------------------------------------------
    # END
    '''
