
def menu():
    """
    """
    scelta=2
    while scelta!=0:
        print("             AGENDA             ")
        print("1--->Intera agenda.")
        print("2--->Programma per quell'orario.")
        scelta=int(input("Inserire 1 o 2: "))
        while scelta<1 or scelta>2:
            scelta=int(input("Inserire 1 o 2"))
        c=carica()
        #if scelta==1:
            #intera(c)
        #else:
            #prog_orario()

def carica():
    """
    """
    for x in range(24):
        scelta=int(input("Inserire  1 se per quell'ora ci sono persone."))
        if scelta==1:
            lista=[]
            orario=x
            nome=str(input("Inserire nome della persona: "))
            programma=str(input("Inserire il programma per quell'ora: "))
            lista.append(orario)
            lista.append(nome)
            lista.append(programma)
    print (lista)









#main
menu()