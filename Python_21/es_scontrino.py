#stampare lo scontrino della spesa, ogni elemento deve avere la descrizione


def menu():
    """
    """
    ogg=oggetti()
    costo(ogg[0],ogg[1])

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
    totale = (tutti, costo)
    return totale

def costo(oggetti, costi):
    """
    """
    print("I codici vanno da 0 a ", len(oggetti)-1)
    codice=input("Inserire codice: ")
    somma=0
    while codice!="":
        codice = int(codice)
        if codice in oggetti:
            num_ogg=int(input("Inserire quanti oggetti si comprano con questo codice: "))
            elemento=oggetti[codice]
            costo=costi[elemento]*num_ogg
            #print(elemento,"*", num_ogg, " ", costo)
            somma=somma+costo
        else:
            print("Hai sbagliato codice, riprova")
        codice=input("Inserire codice: ")
    scontrino()
    print("TOTALE---->", somma)

#main
menu()