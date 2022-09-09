numero=int(input('Anna jokin numero: '))

for i in range(numero-1, 0, -1):
    if i==1: print('Kyseessä on alkuluku')
    elif numero%i==0: break