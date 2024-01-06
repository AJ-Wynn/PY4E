# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# http://data.pr4e.org/romeo.txt
# http://www.py4e.com/code3/romeo-full.txt
# http://data.pr4e.org/intro-short.txt
# http://data.pr4e.org/romeo-full.txt

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def convert(s):
    str1 = ""
    return(str1.join(s))

while True:
    try:

        url = input("Enter - ")
        fhand = urllib.request.urlopen(url)
        counter = 0
        switch = False
    
        for line in fhand:
            counter = counter + len(line)
            
            if (counter > 3000):
                if switch is False:
                    last_line_overflow = counter - 3000

                    split_line = list(line.decode())
                    last_line_charcount = len(split_line) - last_line_overflow
                    last_line_str = convert(split_line)
                    print(last_line_str[0:last_line_charcount])
                    
                    switch = True
                    #print(counter)

                else:
                    continue
                
            else:
                print(line.decode(), end='')
                #print(counter)

        break

    
    except:
        print("Please enter a valid URL")
        continue
        
    
print("\n")
print("Total number of characters: ", counter)



