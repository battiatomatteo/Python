#data una serie di numeri terminate con 0 visualizzare quanti sono i pari e quanti sono i dispari.
num = int(input())
dis = 0
pari = 0
while num != 0:
    ris = float (num)/2
    resto = num - ris * 2
    if resto == 0:
        pari = pari + 1
    else:
        dis = dis + 1
    num = int(input())
print(pari)
print(dis)
