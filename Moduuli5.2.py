luvut=[]
summa=0
mjono_saatu = True

while mjono_saatu:
    luku = input('Anna luku: ')
    if luku == "":
        mjono_saatu = False
    else:
        luvut.append(float(luku))
        luku = input('Anna luku: ')
luvut.sort(reverse=True)
for luku in (luvut[0:5]):
    print(luku)
