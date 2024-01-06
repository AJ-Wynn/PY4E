import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter URL: ')
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    print(data)
    
    tree = ET.fromstring(data)

    sum = 0
    counts = tree.findall('comments/comment')
    for item in counts:
        count = int(item.find('count').text)
        sum = sum + count

    print('Count:', len(counts))
    print('Sum:', sum)
    break