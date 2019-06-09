"""
Created by: Kr0ff
Date: 2019/06/09

Description: Simple script that takes a given value from the
challenge url and encrypts in using md5 algorithm. The encrypted
value is sent to the url as post request to retrieve the flag.
Cookies the most important part here, since they are needed for
authentication. Cookies change on every page reload just like the
string required for challenge completion.

"""
print("""
 _____  ____   ___
|     ||    \ |  _|
| | | ||  |  ||_  |
|_|_|_||____/ |___|
 ___
| | |
|_  | By: Kr0ff
  |_|
 _  _  ___
| ||_||  _| ___
| || ||  _|| -_|
|_||_||_|  |___|


010011010100010000110101
00110100
01101100011010010110011001100101

""")


import requests
import hashlib
from time import sleep as s
from bs4 import BeautifulSoup

###### MAKE GET REQUST ######
host = requests.get("http://docker.hackthebox.eu:39448") # connect to host with GET
soup = BeautifulSoup(host.text, 'html.parser')
hash = soup.h3.get_text() #output just text between tag <h3>

###### MD5 ENCRYPT THE GIVEN VALUE ######
md5 = hashlib.md5() #use md5 from hashlib
md5.update(hash.encode('utf-8')) #encode value as UTF-8
emdeed = md5.hexdigest() #digest it as hex

###### MAKE THE POST REQUST ######
h = requests.post("http://docker.hackthebox.eu:39448", data={'hash':emdeed}, cookies=host.cookies, allow_redirects=True) #send post request

###### RETRIEVE JUST FLAG ######
flagsoup = BeautifulSoup(h.text, 'html.parser') #parse the date with html.parser
flag = flagsoup.p.get_text() #get value of <p> where flag is placed
s(3)
print("FLAGGGGG ---->>", flag) #FLAG !
