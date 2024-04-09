#esempio di funzione con passaggi di parametri in Python


#definizione della funzione e dei parametri da elaborare

def saluto(nome, cognome):
    print("Ti chiami", nome, " ", cognome, ". Ciao!")
    nome = "gigi"
    cognome = "gigino"
    print("Ti chiami", nome, " ", cognome, ". Ciao!")

#programma principale    
nomeprinc = "homer"
cognomeprinc = "simpson"
#chiamata alla funzione
saluto(nomeprinc, cognomeprinc)
print(nomeprinc, "",cognomeprinc)
