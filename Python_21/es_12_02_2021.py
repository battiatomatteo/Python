#fare un programma dove si ordinano gli elementi presenti in una lista

import random

def menu():
    """
    """
    scelta = -2
    while scelta != 0:
        print("------------------------------")
        print("            Menu              ")
        print("------------------------------")
        print("Scrivi 1 se vuoi un ordinamento per scambio con doublesort: ")
        print("Scrivi 2 se vuoi un ordinamento per scambio con la selezione: ")
        print("Scrivi 3 se vuoi un ordinamento per scambio con l'inserimento: ")
        scelta=int(input("Inserire 1, 2 o 3: "))
        while scelta<1 or scelta>3:
                scelta=int(input("Inserire nuovamente un numero: "))
        if scelta==1:
            doublesort()
        elif (scelta==2):
            selezione()
        elif (scelta==3):
            inserimento()


def doublesort():
    """
    """
    print("Orinamento per scambio (Doublesort)")
    Tanti=int(input("Inserire grandezza lista: "))
    maxValore=int(input("Inserire il massimo valore che può essere inserito: "))
    numeri=[]
    Trovato=False 

    for x in range(Tanti):
        numeri.append(random.randint(1, maxValore));

    print("prima", numeri)
    for x in range(0, Tanti-1):
        for y in range(0, Tanti-1):
            if numeri[y]>numeri[y+1]:
                temp=numeri[y]
                numeri[y]=numeri[y+1]
                numeri[y+1]=temp;

    print("Dopo", numeri)

def selezione():
    """
    """
    print("\nOrdinamento per selezione")
    Tanti=int(input("Inserire grandezza lista: "))
    maxValore=int(input("Inserire il massimo valore che può essere inserito: "))
    numeri=[]
    Trovato=False 
    for x in range(Tanti):
        numeri.append(random.randint(1, maxValore));
    print("Prima", numeri)
    for x in range(0, Tanti):
        i_min = x
        for y in range(x+1, Tanti):
            if numeri[y]<numeri[i_min]:
                i_min=y
        temp=numeri[i_min]
        numeri[i_min]=numeri[x]
        numeri[x]=temp;
        print("Inter", numeri)
    print("Dopo ",numeri)

def inserimento():
    """
    """
    print("\nOrdinamento per inserimento")
    Tanti=int(input("Inserire grandezza lista: "))
    maxValore=int(input("Inserire il massimo valore che può essere inserito: "))
    numeri=[]
    for x in range(Tanti):
        numeri.append(random.randint(1, maxValore));
        if len(numeri) == 0:
            print("\nCarica la lista prima di proseguire\n")
        else:
            print("\nPrima: ", numeri)
            for i in range(1, len(numeri)):
                appoggio = numeri[i]
                prec = i - 1
                while prec >= 0 and numeri[prec] > appoggio:
                    numeri[prec + 1] = numeri[prec]
                    prec -= 1
                numeri[prec + 1] = appoggio
            print("Dopo: ", numeri)

#main
menu()