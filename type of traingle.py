a = int(input('Enter first side'))
b = int(input('Enter second side'))
c = int(input('Enter third side'))
if a + b > c and b + c > a and a + c > b:
    print('Its a triangle')

    if a==b==c :
        print('Its a equilaterial triangle')
    elif a==b or b==c or a==c:
        print('its a isosceles triangle')
    else:
        print('its  a scalene traingle')
else:
    print('its not a traingle')