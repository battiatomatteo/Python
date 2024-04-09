#Stampare una sequenza di 3 nomi usando una funzione

#definizione della funzione
def nomi_persone(nome, cognome):
    #tutte le istruzioni della funzione con nome e cognome come parametri di ingresso
    print("Ti chiami " + nome + " " + cognome + ", Ciao!")

#la funzione si ripete per 3 volte
for i in range(3):
    nome = input("Inserire il nome della persona: ")
    cognome = input("Inserire il cognome della persona: ")
    nomi_persone(nome, cognome)
