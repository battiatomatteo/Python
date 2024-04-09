#stampa rettangolo inserendo nr righe e nr colonne
#nr righe e nr colonne >=3

#innput con controllo valore
print("DISEGNA RETTANGOLO VERSIONE 0")
nr_righe= int(("onserire nr. righe rettangolo(>2) ---> "))
while (nr_righe <3):
    nr_righe= int(("onserire nr. righe rettangolo(>2) ---> "))

nr_col = int(("onserire nr. colonne rettangolo(>2) ---> "))
while (nr_col < 3):
    nr_col = int(("onserire nr. colonne rettangolo(>2) ---> "))
print("\n \n")



#elaboratore con disegno 1 VERSIONE
print("disegno con 1^ versione")
print("*"*nr_righe)                     #prima riga pari a lunghezza colonne
for r in range(1, nr_righe-1):           #gestisce righe
    print("*", sep="")                  #primo carattere di ogni riga >1
    for c in range(1, nr_col-1):
        print("Q", sep="")
    print("")                   #ultimo carattere di ogni riga < righe
print("*"*nr_col)        #ultima riga pari a righe
print("\n")



# elaborazione con disegno 2^ versione
print("disegno con 2^ versione")
for r in range(nr_righe):                  #gestisci righe
    if ( r== 0 ) or (r == nr_righe-1):      #gestione prima e ultima riga
        print("*"*nr_col)
    else:
        for c in range(0, nr_col):          # gestisci contenuti righe (= colonne)
            if (c==0) or (c== nr_col-1):
                print("*", end="")
            else:
                print("Q", end="")
        print("")           # a capo su nuova riga