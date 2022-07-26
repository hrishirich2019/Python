x = int(input('enter basic salary: '))
if x <= 10000:
    y = (x * 0.2) + (x * 0.8) + x
    print('grosss salary', y)
elif x <= 20000:
    y = (x * 0.3) + (x * 0.9) + x
    print('grosss salary', y)
elif x > 20000:
    y = (x * 0.35) + (x * 0.95) + x
    print('grosss salary', y)
