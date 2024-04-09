#creare 3 insiemi, strumenti lavoro sarto, barbiere, elettricista...visualizzare:
#elenco strumenti usati dai professionisti(tutti).
#elenco strumenti comuni.
#possibilità di aggiungere uno strumento a unoi degli insiemi.
#possibilità di eliminare uno strumento da uno degli insiemi.

def menu():
    """
    Creazione del menu
    P. ingresso://
    P.uscita://
    """
    scelta=-1
    while scelta!=0:
        print("         MENU        ")
        print("1)elenco strumenti usati dai professionisti(tutti).")
        print("2)elenco strumenti in comune.")
        print("3)possibilità di aggiungere uno strumento a uno degli insiemi.")
        print("4)possibilità di eliminare uno strumento da uno degli insiemi.")
        print("0)FINE")
        scelta=int(input("Inserire un numero da 1 a 4 o 0 se vuoi finire: "))
        #insiemi
        sarto={"stoffa", "filo", "forbici", "ago"}
        barbiere={"forbici", "rasoio", "spazzola", "pettine"}
        elettricista={"forbici", "cavi", "cacciavite"}
        #controllo scelta
        while scelta<0 or scelta>4:
            scelta=int(input("Scegliere un numero da 1 a 4: "))
        if scelta==1:
            strumenti_usati(sarto,barbiere,elettricista)
        elif (scelta==2):
            elenco(sarto,barbiere,elettricista)
        elif(scelta==3):
            aggiungere(sarto,barbiere,elettricista)
        elif(scelta==4):
            togliere(sarto,barbiere,elettricista)
    print("Arrivederci.")
    

def strumenti_usati(sarto,barbiere,elettricista):
    """
    elenco strumenti usati dai professionisti(tutti)
    P. ingresso: sarto,barbiere,elettricista
    P. uscita://
    """
    print("Prima")
    print("sarto:",sarto,"\nbarbiere: ",barbiere,"\nelettricista",elettricista)
    tutti=[]
    set(tutti)
    tutti=sarto.union(barbiere.union(elettricista))
    print("Dopo: ",tutti)
     

def elenco(sarto,barbiere,elettricista):
    """
    elenco strumenti in comune
    P. ingresso: sarto,barbiere,elettricista
    P. uscita://
    """
    print("Tutti gli strumenti:")
    print("sarto:",sarto,"\nbarbiere: ",barbiere,"\nelettricista",elettricista)
    comune=[]
    set(comune)
    comune=sarto.intersection(barbiere.intersection(elettricista))
    print("Dopo: ",comune)


def aggiungere(sarto,barbiere,elettricista):
    """
    possibilità di aggiungere uno strumento a uno degli insiemi
    P. ingresso: sarto,barbiere,elettricista
    P. uscita://
    """
    print("sarto:",sarto,"\nbarbiere: ",barbiere,"\nelettricista",elettricista)
    scelta=int(input("Scegli quale insieme modificare 1)sarto, 2)barbiere ,3) elettricista: "))
    while scelta<1 or scelta>3:
        scelta=int(input("Scegli quale insieme modificare 1)sarto, 2)barbiere ,3) elettricista: "))
    if scelta==1:
        elemento=str(input("Scrivi l'elemento che vuoi inserire: "))
        sarto.add(elemento)
    elif (scelta==2):
        elemento=str(input("Scrivi l'elemento che vuoi inserire: "))
        barbiere.add(elemento)
    elif (scelta==3):
        elemento=str(input("Scrivi l'elemento che vuoi inserire: "))
        elettricista.add(elemento)
    print("sarto:",sarto,"\nbarbiere: ",barbiere,"\nelettricista",elettricista)

def togliere(sarto,barbiere,elettricista):
    """
    possibilità di eliminare uno strumento da uno degli insiemi
    P. ingresso: sarto,barbiere,elettricista
    P. uscita://
    """
    print("sarto:",sarto,"\nbarbiere: ",barbiere,"\nelettricista",elettricista)
    scelta=int(input("Scegli quale togliere nell'insieme 1)sarto, 2)barbiere ,3) elettricista: "))
    while scelta<1 or scelta>3:
        scelta=int(input("Scegli quale insieme modificare 1)sarto, 2)barbiere ,3) elettricista: "))
    if scelta==1:
        elemento=str(input("Scrivi l'elemento che vuoi togliere: "))
        sarto.discard(elemento)
    elif (scelta==2):
        elemento=str(input("Scrivi l'elemento che vuoi togliere: "))
        barbiere.discard(elemento)
    elif (scelta==3):
        elemento=str(input("Scrivi l'elemento che vuoi togliere: "))
        elettricista.discard(elemento)
    print("sarto:",sarto,"\nbarbiere: ",barbiere,"\nelettricista",elettricista)

#main
menu()