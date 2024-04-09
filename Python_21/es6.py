#Uno studente esamina le informazioni sulle verifiche scritte fatte; si desidera sapere quante sono le prove sufficienti.
n = int(input())
suff = 0
for v in range(1, n + 1, 1):
    voto = int(input())
    if voto >= 6:
        suff = suff + 1
print(suff)        
