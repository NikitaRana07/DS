print('Welcome! to the game you wish had never played \n(this is the most rediculous game you wil ever play)');
number=1
while number<4:

    g=input('Enter any number to know whats in store for you.');
    try:
         g1=int(g)
    except:
         print('Please be polite and enter the thing you are asked to please enter a number.\n it might not be your fault entirely but i really want to write so i did')
         continue
    if g1!=5:
        print('You are a blody bastard!');
    else:
        print('You are the father of the universe you have got to save the world.')
    number+=1;
