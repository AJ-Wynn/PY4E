# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

first_url = input('Enter URL: ')
repeat = input('Enter repeat number: ')
position = input('Enter position: ')

url = first_url

for i in range(int(repeat)):

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    url_list = list()

    # Store href values in a list
    for tag in tags:
        href_value = tag.get('href', None)
        url_list.append(href_value)
    
    url = url_list[int(position) - 1]

name = re.findall('known_by_(.+).html', url)
print(name[0])