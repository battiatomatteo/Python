#data una lista con solo quattro elementi distinti (es "mela", "pera", "ciliegia", e "fragola"),
#crea un'altra lista dove ogni elemento è una tupla contenente il nome del frutto
#e il numero di volte che compare nella lista originale (=molteplicita)


def menu():
    """
    P. ingresso: //
    P. uscita: //
    """
    c=carica()
    print("Prima")
    stampa(c)
    n=numera(c)
    print("Dopo")
    stampa(n)

def carica():
    """
    Carica la lista
    P. ingresso: //
    P. uscita: lista
    """
    lista=["mela", "pera", "mela", "ciliegia", "pera", "mela", "pera", "pera",  "ciliegia", "pera", "fragola"]
    return lista

def stampa(x):
    """
    Stampa a video la lista
    P. ingresso: x
    P. uscita: //
    """
    print(x)

def numera(lista):
    """
    Conta quante volte gli elementi sono presenti nella lista
    P. ingresso: lista
    P. uscita: lista
    """
    tuplam=("mela", lista.count("mela"))
    tuplap=("pera", lista.count("pera"))
    tuplaf=("fragola", lista.count("fragola"))
    tuplac=("ciliegia", lista.count("ciliegia"))
    lista=[tuplam, tuplap, tuplaf, tuplac]
    return lista


#main program
menu()


"""
#lista iniziale
parole= ["mela", "pera", "mela", "ciliegia", "pera", "mela", "pera", "pera",  "ciliegia", "pera", "fragola"]

#creazione tuple
conta_mela = ("mela", lista.count("mela"))
conta_pera = ("pera", lista.count("pera"))
conta_ciliegia = ("ciliegia", lista.count("ciliegia"))
conta_fragola = ("fragola", lista.count("fragola"))

#costruzione lista da tuple
lista_finale = [conta_mela conta_pera conta_ciliegia conta_fragola]

#stampa di lista finale
print(lista_finale)
lista_finale[0] = "frutta"
"""