from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
i=int(input("Enter the position"))
j=int(input("Enter the count")) 
while j!=0:
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    
    count=0
    # Retrieve all of the anchor tags
    tags = soup('a')

    for tag in tags:
        # Look at the parts of a tag
        count=count+1;
        if count==i:
            url=tag.get('href', None)
            print('URL:', tag.get('href', None))
            print('Contents:', tag.contents[0])
            break
    j=j-1
