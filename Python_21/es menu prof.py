"""
menu scelta operazioni da svolgere
ingresso//
uscita//
"""
lista=[]
scelta = -1
while (scelta !=0):
    print("---------------------------------")
    print("    OPERAZIONI CON LE LISTE     ")
    print("---------------------------------")
    print("     1 - inserimento ")
    print("     2 - stampa lista completa ")
    print("     3 - stampa elemnti posizione pari/dispari ")
    print("     4 - stampa lista completa con indice negativo ")
    print("     5 - aggiungi elemento ")
    print("     6 - inserimento elemento in posizione scelta ")
    print("     7 - ricerca elemento ")
    print("     8 - posizione elemento cercato ")
    print("     0 - fine lavoro ")
    scelta = int(input("scelta (0-8) ---> "))
    if (scelta == 1):
        lista  = inserimento(lista)
    elif(scelta == 2):
        stampa(lista)
    elif(scelta == 3):
        pos = int(input("inserire 0 pari - 1 dispari -->"))
        stampa_pos(pos, lista)
    elif(scelta == 4):
        stampa_neg(lista)
    elif(scelta == 5):
        aggiunta(lista)
    elif(scelta == 6):
        inserire(lista)
    elif(scelta == 7):
        cerca(lista)
    elif(scelta == 8):
        pos_cerca(lista)
    else:
        print("Ciao, riposati!")

def inserimento(elenco):
    """
    caricamento valori elementi della lista
    ingresso: lista vuota
    uscita: elenco con lista caricata
    """
    elenco = [1, 2, 3, 4, 5]
    return elenco
def stampa(elenco):
    """
    visualizare valori elementi della lista
    ingresso: lista 
    uscita: //
    """
    if (len(elenco) == 0):
        print("non ci sono elementi nella lista (LISTA VUOTA), scegliere 1 dal menu")
    else:
        print("Elementi della lista \n", elenco)
        print("---------------1 versione ---------------------")
        for element in elenco:
            print(element)
        print("---------2 versione-------------")
        for i in range(5):
            print(elenco[i])

def stampa_pos(pos, elenco):
   pass

def stampa_neg(elenco):
   pass

def aggiunta(elenco):
   pass

def inserire(elenco):
   pass

def cerca(elenco):
   pass

def pos_cerca(elenco):
   pass

#main program
main()
        
