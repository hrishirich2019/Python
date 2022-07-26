Actual = int(input('enter actaul cost'))
Selling = int(input('enter selling cost'))
if Selling > Actual:
    print('profit')
elif Actual > Selling:
    print('Loss')
else:
    print('no profit no loss')
