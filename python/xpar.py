import urllib.request, urllib.parse,urllib.error
import xml.etree.ElementTree as ET
url=input("Enter the URL:")
fhand=urllib.request.urlopen(url)

suma=0
coun=0
data=''''''
for line in fhand:
    data=data+line.decode()

#print(data)

tree=ET.fromstring(data)
counts = tree.findall('.//count')
i=0
for count in counts:
    #print(count)
    #print(int(counts[i].text))
    suma=suma+int(counts[i].text)
    i=i+1
    coun=coun+1

print("SUM:",suma)
print("COUNT:",coun)
