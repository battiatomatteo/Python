# una lista di num interi, controllare il numero di elementi( deve essere pari) e spostare la prima metà al posto della seconda metà

import random

def creazione():
    """
    In questa funzione si crea una lista e si controlla che il numeri di elementi sia pari
    Parametri in ingresso: //
    Parametri in uscita: 1
    """
    lista=[]
    x=int(input("Inserire grandezza lista: "))
    while x%2!=0:                                                   #controllo se la lista è pari o dispari
        x=int(input("Inserire grandezza lista: "))
    
    y=int(input("Inserire il numero minimo che può oessere inserito: "))
    w=int(input("Inserire il numero massimo che può oessere inserito: "))
    for i in range(x):
        lista.append(random.randint(y, w))
    
    print("Prima", lista)
    return lista


def scambio(lista):
    """
    In questa funzione scambio la prima metà della lista con la seconda
    Parametri in ingresso: 1
    Parametri in uscita: 1
    """
    meta=int(len(lista)/2)
    for i in range(meta):
        appoggio=lista[i]
        lista[i]=lista[i+meta]
        lista[i+meta]=appoggio

    print("Dopo", lista)
    


#main program

c=creazione()
scambio(c)










"""
metà=len(lista)/2
    for i in range(metà):
        appoggio=lista[i]
        lista[i]=lista[i+metà]
        lista[i+metà]=appoggio
"""