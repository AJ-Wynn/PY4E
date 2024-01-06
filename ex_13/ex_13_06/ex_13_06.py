# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

count = 0
span_tag_sum = 0

# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    tagvalue = int(tag.text)
    count += 1
    span_tag_sum += tagvalue

print("Count", count)
print("Sum", span_tag_sum)
   