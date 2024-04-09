#scrivi un programma che dopo aver riempito con numeri casuali un vettore di numele elementi con valori compresi tra max e min
#verifica  se gli elemnti in posizione pari sono pari e quelli dispari nei dispari
#indica quanti numeri sono in posizione errata

import random
numeri=[]
errati= 0
elementi=20
max= 1000
min=0

for i in range (0, elemtni+1)
    num= random.radint(min,max)
    numeri.append(num)
    if (i % 2 == 1 and num % 2 == 0 ) or (i % 2 == 1 and num % 2 == 1)
     pass
    else:
        errati +- 1

print(numeri)
print("il num. di numeri al posto errato sono: " errati)