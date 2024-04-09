#scrivi un programma che generi casualmente 30 nume li memorizzi in due liste
#prima lista --->numeri pari
#seconda lista --->numeri dispari

import random

def inserimento(listap, listad):
    """
    Parametri in ingresso:2
    Parametri in uscita:2
    """
    for i in range(30):
        num=random.randint(0, 1000)
        if num%2==0:
            listap.append(num)
        else:
            listad.append(num)
    print(listap)
    print(listad)

#main
listap=[]
listad=[]
inserimento(listap, listad)