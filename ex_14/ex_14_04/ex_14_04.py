import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input("Enter URL: ")
    if len(url) < 1:
        break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    # print(data)


    info = json.loads(data)
    print('User count:', len(info['comments']))
    sum = 0
    # print(info)
    for item in info['comments']:
        count = item['count']
        sum = sum + int(count)

    print('Sum:',sum)
    break