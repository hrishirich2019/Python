phy = int(input('enter physics marks: '))
chem = int(input('enter chem marks: '))
bio = int(input('enter bio marks: '))
maths = int(input('enter maths marks: '))
cs = int(input('enter cs marks: '))
per = ((phy + chem + bio + maths + cs) / 500) * 100
print(per, '%')

if per >= 90:
    print('Grade A')
elif per >= 80:
    print('Grade B')
elif per >= 70:
    print('Grade C')
elif per >= 60:
    print('Grade D')
elif per >= 40:
    print('Grade A')
else:
    print('fail')
