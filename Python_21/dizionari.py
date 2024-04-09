#i dati dei prodotti venduti di un'azienda commerciale 
#sono rappresentati con una chiave , costituita da un codice numerico intero,
#e una descrizione del prodotto,
#successivamnente si deve stampare ogni prodotto con la sua descrizione

def inserimento():
    """
    con la funzione inserimeno si assegnano al dizionario prodotti il nome e il codice di ogni singolo prodotto
    parametri in ingresso: nessuno
    parametri in uscita: prodotti(il dizionario con le coppie di codice prodotto)
    """
    prodotti = {}
    numero_prodotti = int(input("Inserire il numero degli elementi che verranno inseriti."))
    while numero_prodotti<0:
         numero_prodotti = int(input("Inserire il numero degli elementi che verranno inseriti."))
    for i in range(numero_prodotti):
        cod = codice_prodotto()
        if sostituzione_valore(cod,prodotti):
            continue
        else:
            nome = nome_prodotto()
        prodotti[cod] = nome
    return prodotti

def codice_prodotto():
    """
    con la funzione codice_prodotto si chiede quale è il codice del prodotto 
    parametri in ingresso: nessuno
    parametri in uscita: codice(il codice del prodotto)
    """
    codice = input("inserire il codice numerico del prodotto\n")
    while not(codice.isdigit()):
        print("possono essere accettati codici formati solo da numeri")
        codice = input("inserire il codice numerico del prodotto\n")
    return codice


def sostituzione_valore(codice,prodotti):
    """
    con la funzione sostituzione_valore si controlla se la chiave inserita è già presente nel dizionario
    parametri in ingresso: codice(il codice assegnato al prodotto), prodotti (il dizionario con i prodotti)
    parametri in uscita: True o False
    """
    lista_chiavi = prodotti.keys()
    affermazioni = ("Sì", "Si", "sì", "si", "SI", "SÌ", "sI", "sÌ")
    if(codice in lista_chiavi):
        print("il codice è già presente")
        risposta = input("si vuole sostituire il codice esistente?\n Sì\tNo\n")

        #se la risposta corrisponde a una possibile forma di sì,
        #allora si sostituisce il vecchio valore con quello nuovo (True),
        #altrimenti si lascierà la coppia vecchia (False) 

        if(risposta not in affermazioni):
            return True 
        else:
            return False        

def nome_prodotto():
    """
    con la funzione sostituzione_valore si chiede quale è il nome del prodotto 
    parametri in ingresso: nessuno
    parametri in uscita: nome(il nnome del prodotto)
    """
    nome = input("inserire il nome del prodotto\n")
    #si continua a chiedere il nome del prodotto fino a che non si inserisce un nome che non sia vuoto
    while(nome == ""):
        print("il nome del prodotto non può essere vuoto")
        nome = input("inserire il nome del prodotto\n")
    return nome

def stampa(prodotti):
    """
    con la funzione stampa si scrivono tutti i valori del dizionario
    parametri in ingresso: prodotti (il dizionario con i prodotti)
    parametri in uscita: nessuno
    """
    #si ripete la  stampa per ogni valore del dizionario
    for i in sorted(prodotti):
        #si stampa la coppia chiave-valore
        print("Il prodotto", prodotti[i], "ha il codice", i)

def main():
    oggetti = inserimento()
    stampa(oggetti)

#main 
main()