import urllib.request, urllib.parse,urllib.error
import json
url=input("Enter the URL:")
fhand=urllib.request.urlopen(url)

suma=0
coun=0
data=fhand.read().decode()
#for line in fhand:
#    data=data+line.decode()

#print(data)

info=json.loads(data)

for item in info["comments"]:
    suma=suma+int(item["count"])
    coun=coun+1

print("SUM:",suma)
print("COUNT:",coun)
