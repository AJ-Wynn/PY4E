# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import socket
from bs4 import BeautifulSoup
import ssl
# http://data.pr4e.org/romeo.txt
# https://www.py4e.com/code3/romeo-full.txt

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    try:

        url = input("Enter - ")
        url_list = url.split("/")
    
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect( (url_list[2], 80))
        cmd = ('GET '+url+' HTTP/1.0\r\n\r\n').encode()
        mysock.send(cmd)

        while True:
            data = mysock.recv(512)
            if (len(data) < 1):
                break
            print(data.decode(), end='')

        mysock.close()
        break

    except:
        print("Please enter a valid URL")
        continue


