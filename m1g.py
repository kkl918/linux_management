import os, datetime, time, pathlib, re
import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from requests.auth import HTTPBasicAuth


path = r'C:\Users\Owner\Desktop\\'
#pathlib.Path(path).mkdir(parents=True, exist_ok=True)

url_rebt = 'http://192.168.10.1/submit.php'
data     = 'REBOOT=TRUE'

url  = 'http://192.168.10.1/record/'
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

def m1g_reboot():
	requests.post(url_rebt, data = {'REBOOT':'TRUE'})
	
