x = input("enter your choice:1. side,2. angle")
if x == '1':
    a = int(input('Enter first Side'))
    b = int(input('Enter second side'))
    c = int(input('Enter third side'))
    if a + b > c and b + c > a and a + c > b:
        print('Its a triangle')
    else:
        print('its not a traingle')
elif x == '2':
    a = int(input('Enter first angle:'))
    b = int(input('Enter second angle:'))
    c = int(input('Enter third angle:'))
    if a + b + c == 180:
        print('Its a triangle')
        if a == b == c:
            print('equilateral ')
        elif a == b or a == c or b == c:
            print('isocesles')
        else:
            print('irregular ')
    else:
        print('its not a traingle')
