unit = int(input('enter number of units: '))
if unit <= 50:
    print('electricity bill', (unit * 0.50) * 1.17)
elif 50 < unit <= 150:
    print('electricity bill', (unit * 0.75) * 1.17)
elif 150 < unit <= 250:
    print('electricity bill', (unit * 1.25) * 1.17)
elif unit > 250:
    print('electricity bill', unit * 1.5 * 1.17)
