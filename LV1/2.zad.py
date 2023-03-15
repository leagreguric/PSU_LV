broj=float(input("Uneite broj: "))
while broj<0.0 or broj>1.0:
    broj=float(input("Unesite broj: "))

if broj>=0.9:
    print('A')
elif broj>=0.8:
    print('B')
elif broj>=0.7:
    print('C')
elif broj>=0.6:
    print('D')
else:
    print('F')