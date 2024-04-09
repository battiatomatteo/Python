#scrivere un programma che utilizzando le funzioni permetta di:
#scambiare tra loro il primo e l'ultimo elemento della lista
#far scorrere tutti gli elementi di una posizione verso destra, spostando l'ultimo elemento nella prima posizione.
#Es. la lista   1 4 9 16 25    diventerà    25 1 4 9 16 

def menu():
    """
    scegliere se scambiare il primo e l'ultimo num o aumentare la posizione di tutti i mun di 1
    parametri in ingresso //
    parametri in uscita 1 
    """
    print("Scrivi 1 se vuoi scambiare tra loro il primo e l'ultimo elemento della lista.")
    print("Scrivi 2 se vuoi far scorrere tutti gli elementi di una posizione verso destra, spostando l'ultimo elemento nella prima posizione.")
    scelta=int(input("Inserire 1 o 2: "))
    while scelta<1 or scelta>2:
        scelta=int(input("Inserisci 1 o 2! "))
    if scelta==1:
        print(scambia())
    else:
        print(scorri())


def scambia():
    """
    scambiare tra loro il primo e l'ultimo elemento della lista
    parametri in ingresso //
    parametri in uscita 1 
    """
    lista=[]
    x=int(input("inserire grandezza lista: "))
    for i in range(x):
        num=int(input("inserire numero intero: ")) 
        lista.append(num)    
    primo=lista[0]
    ultimo=lista[-1]
    lista[0]=ultimo
    lista[-1]=primo
    return lista


def scorri():
    """
    far scorrere tutti gli elementi di una posizione verso destra, spostando l'ultimo elemento nella prima posizione.
    parametri in ingresso //
    parametri in uscita 1 
    """
    lista=[]
    x=int(input("inserire grandezza lista: "))
    for i in range(x):
        num=int(input("inserire numero intero: ")) 
        lista.append(num)
    ultimo=lista[-1]
    """
    a=0
    while a!=x:
        primo=lista[a]
        a=a+1
        secondo=lista[a]
        lista[a]=primo
        pr=secondo
    """
    lista[0]=ultimo
    return lista
    

#programma
menu()
