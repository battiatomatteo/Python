#Ci sono 3 negozi, per ogni negozio si usa una lista per gli incassi della settimana (da lunedì a domenica). Visualizzare con un funzione
#, utilizzando una tupla, gli incassi specificando i giorni della settimana --- si usa una tupla per la definizione dei giorni.
#Successivamente fare una funzione per gli incassi settimanali.

import random

def main():
    """
    Mi crea un medu a più scelte
    P. ingresso: //
    P: uscita: //
    """
    ins=inserimento()
    tupla=("Lunedì", "Martedì" , "Mercoledì" , "Giovedì", "Venerdì", "Sabato", "Domenica")
    stampa_totale(ins, tupla)

def stampa_totale(lista, giorni):

    print("\n-------Questi sono gli incassi della settimana------\n")

    for i in range(0,len(giorni)):
        print(giorni[i], end =" ")

    print()
    for r in range(0,3,1):
        for c in range(0,7,1):
            print(" ",lista[r][c], end = "\t")
        print("negozio ", r + 1)

def inserimento():
    """
    Inserimento degli incassi 
    P. ingresso: //
    P. uscita: 1
    """
    matrice= [
              [0]*7,
              [0]*7,
              [0]*7,
              [0]*7
             ]
    for a in range(4):
        for i in range(7):
            num=random.randint(0, 100)
            matrice[a][i]=num

    return matrice



[0]*7
#programma principale
main()