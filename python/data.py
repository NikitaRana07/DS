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

suma=0
count=0
# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    
    count=count+1
    suma=suma+int(tag.contents[0]);
    print('Content:', tag.contents[0])
   

print(suma,count)
