#con 4 liste (una per settimana) visualizzare una lista con tutti gli incassi 

import random

def menu():
    """
    in questo menu si può scegliere come visualizzare gli incassi
    parametri in ingresso: //
    paametri in usita: 1
    """
    scelta = -2
    while scelta != 0:
        print("--------------------")
        print("        MENU        ")
        print("--------------------")
        print("Digita 0 se vuoi vedere gli incassi in 4 liste, una per settimana")
        print("Digita 1 se vuoi vedere gli incassi in una sola lista")
        scelta=int(input("Inserire un numero: "))
        while scelta<0 or scelta>1:
            scelta=int(input("Inserire nuovamente un numero: "))
        if (scelta==1):
            mese()
        elif(scelta==0):
            settimane()
        

def settimane():
    """
    stampa a video 4 liste, in ognuna di esse ci sono gli incassi della settimana
    parametri in ingresso: //
    parametri in uscita: 1
    """
    lista1=[]
    for i in range(7):
        lista1.append(int(random.randint(10, 100)))
    lista2=[]
    for i in range(7):
        lista2.append(int(random.randint(10, 100)))
    lista3=[]
    for i in range(7):
        lista3.append(int(random.randint(10, 100)))
    lista4=[]
    for i in range(7):
        lista4.append(int(random.randint(10, 100)))
    print("Gli incassi delle 4 settimane sono:\n", lista1, "\n", lista2, "\n", lista3, "\n", lista4)
    return lista1, lista2, lista3, lista4

#main
menu()