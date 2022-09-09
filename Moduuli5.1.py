import random
summa=0

for i in range(int(input('Anna arpakuutioiden lukumäärä: '))):
    summa+=random.randint(1, 6)
print("Silmälukujen summa on: " ,summa,)