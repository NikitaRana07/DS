print('Here you can add your numbers')
a=None
while True:
	a=input('Enter the number to add')
	if a is 'Done' or a is 'done' or a is 'DONE':
        break
	try:
		a1=float(a)
	except:
		print('Enter numeric value.')
		continue
	a1=a1+a1
print (a1)
