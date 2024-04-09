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
        print("Digita 1 se vuoi vedere gli incassi in una sola lista")
        print("Digita 2 se vuoi vedere gli incassi in 4 liste, una per settimana")
        print("Digita 3 se vuoi vedere gli incassi della prima settimana")
        print("Digita 4 se vuoi vedere gli incassi della seconda settimana")
        print("Digita 5 se vuoi vedere gli incassi della terza settimana")
        print("Digita 6 se vuoi vedere gli incassi della quarta settimana")
        scelta=int(input("Inserire un numero: "))
        while scelta<1 or scelta>7:
            scelta=int(input("Inserire nuovamente un numero: "))
        if (scelta==1):
            mese()
        elif(scelta==2):
            settimane()
        elif(scelta==3):
            prima()
        elif(scelta==4):
            seconda()
        elif(scelta==5):
            terza()
        elif(scelta==6):
            quarta()


def mese():
    """
    stampa a video una lista con tutti gli incassi del mese
    parametri in ingresso: //
    parametri in uscita: 1
    """
    lista=[]
    y=int(input("Inserire i giorni del mese: "))  
    for i in range(y):
        lista.append(int(random.randint(10, 100)))
    print(lista)

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
    

def prima():
    """
    stampa a video gli incassi della prima settimana
    parametri in ingresso: //
    patametri in uscita: 1
    """
    lista = []
    for i in range(6):
        lista.append(int(random.randint(10, 100)))
    print("\nIncassi prima settimana:\n", lista)

def seconda():
    """
    stampa a video gli incassi della seconda settimana
    parametri in ingresso: //
    patametri in uscita: 1
    """
    lista = []
    for i in range(6):
        lista.append(int(random.randint(10, 100)))
    print("\nIncassi seconda settimana:\n", lista)

def terza():
    """
    stampa a video gli incassi della terza settimana
    parametri in ingresso: //
    patametri in uscita: 1
    """
    lista = []
    for i in range(6):
        lista.append(int(random.randint(10, 100)))
    print("\nIncassi terza settimana:\n", lista)

def quarta():
    """
    stampa a video gli incassi della quarta settimana
    parametri in ingresso: //
    patametri in uscita: 1
    """
    lista = []
    for i in range(6):
        lista.append(int(random.randint(10, 100)))
    print("\nIncassi quarta settimana:\n", lista)

#def matrice():
    """
    creazione della matrice con al suo interno gli incassi suddivisi in 4 settimane da 6 giorni
    parametri in ingresso://
    parametro in uscita: 1
    """ 
#    return matrice 

#programma
menu()
