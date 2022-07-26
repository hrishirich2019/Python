a = int(input('Enter first Side'))
b = int(input('Enter second side'))
c = int(input('Enter third side'))
if a + b > c and b + c > a and a + c > b:
    print('Its a triangle')
else:
    print('its not a traingle')
