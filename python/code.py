import re
fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
	lst=re.findall(r'\d{1,9}',line)
	if lst!=[]:
		for n in lst:
			count=count+int(n)
    
print("The sum is ", count)

