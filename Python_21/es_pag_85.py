import random

def inserimento(lista, x):
    """
    Questa funzione crea una lsita e controlla i valori al suo intenro
    Ingresso: lista, x
    Usita: lista
    """
    w=int(input("Inserire il valore minimo: "))
    z=int(input("Inserire il valore massimo: "))
    for i in range(x):
        lista.append(random.randint(w, z))
    #controllo
    for i in range(x):
        y=1
        while lista[i] == lista[y]:
            lista[i]=int(input("Inserire un nuovo numero: "))
            y +=1

    return lista


def scambio(lista, x):
    """
    Questa funzione permette di scambiare il valore massimo e il valore minimo della lista
    Ingresso: lista, x
    Uscita: nuova lista
    """
    """
    max(lista)
    min(lista)
    return lista
    """
    massimo=lista[0]
    for i in range(x):                                  
        if lista[i]>massimo:
            massimo=lista[i]
            posizione1=i

    minore=lista[0]
    for i in range(x):
        if lista[i]<minore:                             
            minore=lista[i] 
            posizione2=i 

    lista[posizione1]=minore
    lista[posizione2]=massimo
    return lista
    
#main
lista=[]
x=int(input("Inserire la capienza della lista: "))
ins=inserimento(lista, x)
print(ins)
sc=scambio(ins, x)
print(sc)











"""

massimo=lista[0]
    for i in range(x):                                  
        if lista[i]>massimo:
            massimo=lista[i]

    minore=lista[0]
    for i in range(x):
        if lista[i]<minore:                             
            minore=lista[i]
"""