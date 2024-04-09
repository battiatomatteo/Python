def menu():
    """
    scegli se spostare i volori presenti nella lista di una posizione verso destra o sinistra
    parametri in ingresso: //
    parametri in usciuta: 1
    """
    print("--- MENU ---")
    print("Inserire 1 se vuoi spostare gli elementi della lista verso destra")
    print("Inserire 2 se vuoi spostare gli elementi della lista verso sinistra")
    scelta=int(input("Inserire 1 o 2: "))
    while scelta<1 or scelta>2:
        scelta=int(input("Inserire 1 o 2: "))
    if scelta==1:
        print(destra(lista()))
    else:
        print(sinistra(lista()))

def lista():
    """
    crea una lista
    parametri in ingresso: //
    parametri in uscita: 1
    """
    lista=[]
    x=int(input("Inserire dimensione lista: "))
    for i in range(x):
        num=int(input("inserire numero intero: ")) 
        lista.append(num) 
    return lista

def sinistra(lista):
    """
    sposta i volori presenti nella lista di una posizione verso sinistra
    parametri in ingresso:1
    parametri in uscita:1
    """
    
    pass

def destra(lista):
    """
    sposta i volori presenti nella lista di una posizione verso destra
    parametri in ingresso:1
    parametri in uscita:1
    """
    ultimo=lista[-1]
    e=0
    for i in range(len(lista)):
        primo=lista[e]
        e +=1
        secondo=lista[e]
        lista[e]=primo




#main
menu()