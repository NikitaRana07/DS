largest = None
smallest = None
#num = input('Enter a number: ')
while True:
    num = input('Enter a number: ')
    if num == 'done':    
        break 
    try:
        fnum=int(num)

    except:
        print ('Invalid input')

        continue
    if largest is None:
        largest=fnum
    else:
        if largest<fnum:
            largest=fnum


    if smallest is None:
        smallest=fnum
    else: 
        if smallest>fnum:
            smallest=fnum   

print('Maximum is ',largest)
print('Minimum is ',smallest)
