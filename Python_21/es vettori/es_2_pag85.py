#scrivi un programma che generi 30 numeri e li memorizzi in due vettori
#  il primo vettore deve contenere solo i numeri pari
# il secodno vettore deve contenere solo i numeri dispari 

import random

pari = []
dispari = []

for i in range(0, 30):
    num = random.randint(0, 100)
    if num % 2 == 1:
        dispari.append(num)
    else:
        pari.append(num)

print("Vettore con i numeri pari: ", pari)
print("Vettore con i numeri dispari: ", dispari)
