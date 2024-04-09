
#stampare lo scontrino della spesa, ogni elemento deve avere la descrizione


def menu():
    """
    """
    ogg=oggetti()#avevi assegnato a ogg i due valori di ritorno senza metterli in una tupla e il programma ad ogg assegnava solo il primo dei due e l'altro veniva perso
    costo(ogg[0],ogg[1])#passavi al programma solo un parametro quando la funzione nella definizione ne voleva 2
    scontrino()
    

def scontrino():
    """
    """
    print("-"*20)
    print("     SCONTRINO")
    print("-"*20)
    

def oggetti():
    """
    """
    tutti={}
    costo={}
    x=int(input("Inserire quanti oggetti sono presentio nel negozio: "))
    for i in range(x):
        codice=i
        oggetto=input("Inserire oggetto: ")
        val=float(input("Inserire valore dell'oggetto: "))
        tutti[codice]=oggetto
        costo[oggetto]=val
    totale = (tutti, costo)#ho messo in una tupla perchè dovevi restituire i due valore ad una unica variabile
    return totale

def costo(oggetti, costi):
    """
    """
    print("I codici vanno da 0 a ", len(oggetti))
    codice=input("Inserire codice: ")#ho tolto la conversione in intero perchè se tu non mettevi nulla quello che ti veniva dato in input era "" e questa stringa se veniva inserita bloccava il programma perchè non poteva essere convertita in intero
    somma=0
    while codice!="":
        #codice = int(input("Inserire codice: ")) #questo non serve perchè fa si che venga chiesto a vuoto una volta in più
        codice = int(codice)#per fare si che il programma funzioni il valore(dopo che è stato controllato viene convertito in intero)
        if codice in oggetti:
            num_ogg=int(input("Inserire quanti oggetti si comprano con questo codice: "))
            elemento=oggetti[codice]
            costo=costi[elemento]*num_ogg
            print(elemento, " ", costo)
            somma=somma+costo
        else:
            print("Hai sbagliato codice, riprova")
        codice=input("Inserire codice: ")#stesso motivo di riga 39
    print("TOTALE---->", somma)

#main
menu()