#* Scrivere un programma che utilizzando un menù fa le seguenti operazioni
#*1) ! crea una lista e cerca se all'interno della lista è presente un valore dato dall'utente
#*2)crea una lista e poi la ordina con il metodo bubble sort.
#*3)crea una lista e poi la ordina seconda l'ordinamento per selezione
#*4)crea una lista ordinandola direttamente mentre la creo.

import random

def main():
    """
    Creazione di un menu a 4 scelte
    P. ingresso: //
    P. uscita: //
    """
    print("--------------------------------------------")
    print("|                  MENU                    |")
    print("--------------------------------------------")
    print("-Inserire 1 per crea una lista e cerca se all'interno della lista è presente un valore dato dall'utente.")
    print("-Inserire 2 per crea una lista e poi la ordina con il metodo bubble sort.")
    print("-Inserire 3 per crea una lista e poi la ordina seconda l'ordinamento per selezione.")
    print("-Inserire 4 per crea una lista ordinandola direttamente mentre la si crea.")
    scelta=int(input("\nInserire 1, 2, 3 o 4: "))
    while scelta<1 or scelta>4:
        scelta=int(input("Inserire 1, 2, 3 o 4: "))
    if scelta==1:
        cerca()
    elif (scelta==2):
        ordinamentods()
    elif (scelta==3):
        ordinamentos()
    elif (scelta==4):
        ordinamento()


def cerca():
    """
    Crea una lista e cerca se all'interno della lista è presente un valore dato dall'utente
    P. ingresso: //
    P. uscita: //
    """
    lista=[]
    x=int(input("inserire grandezza lista: "))
    for i in range(x):
        lista.append(random.randint(0, 100))
    print(lista)
    num=int(input("Inserire il numero che desidera trovare: "))
    if num in lista:
        print("Questo numero è presente nella lista.")
    else:
        print("Questo numero non è presente nella lista.")

def ordinamentods():
    """
    Crea una lista e poi la ordina con il metodo bubble sort.
    P. ingresso: //
    P. uscita: //
    """
    x=int(input("Inserire grandezza lista: "))
    numeri=[]
    Trovato=False 
    for x in range(x):
        numeri.append(random.randint(1,100))

    print("prima", numeri)
    for x in range(0, x-1):
        for y in range(0, x-1):
            if numeri[y]>numeri[y+1]:
                temp=numeri[y]
                numeri[y]=numeri[y+1]
                numeri[y+1]=temp
    print("Dopo", numeri)


def ordinamentos():
    """
    crea una lista e poi la ordina seconda l'ordinamento per selezione
    P. ingresso: //
    P. uscita: //
    """
    x=int(input("Inserire grandezza lista: "))
    numeri=[]
    Trovato=False 
    for x in range(x):
        numeri.append(random.randint(1, 100))
    print("Prima", numeri)
    for x in range(0, x):
        i_min = x
        for y in range(x+1, x):
            if numeri[y]<numeri[i_min]:
                i_min=y
        temp=numeri[i_min]
        numeri[i_min]=numeri[x]
        numeri[x]=temp
        print("Inter", numeri)
    print("Dopo ",numeri)


def ordinamento():
    """
    Crea una lista ordinandola direttamente mentre la creo.
    P.ingresso: //
    P. scita: //
    """
    x=int(input("Inserire grandezza lista: "))
    lista=[]
    for x in range(x):
        lista.append(random.randint(1,100))
        if len(lista) == 0:
            print("\nCarica la lista prima di proseguire\n")
        else:
            print("\nPrima: ", lista)
            for i in range(1, len(lista)):
                appoggio = lista[i]
                prec = i - 1
                while prec >= 0 and lista[prec] > appoggio:
                    lista[prec + 1] = lista[prec]
                    prec -= 1
                lista[prec + 1] = appoggio
            print("Dopo: ", lista)


#main program
main()