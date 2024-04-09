#costrire un app che attraverso un menu permetta all'utente di scegliere tra le seguenti possibilità
#visualizzazione del numero di divisori di un intero
#visualizzazione dell'elevamento a potenza di un intero dopo averne inserito l'esponente
#verifica se è un numero primo

#obbligo di strutturatrare il codice utilizzando le funzioni

def menu(num):
    """
    parametri in ingresso:1
    parametri in uscita:1
    """
    print("1:visualizzazione del numero di divisori di un intero")
    print("2:visualizzazione dell'elevamento a potenza di un intero dopo averne inserito l'esponente")
    print("3:verifica se è un numero primo")
    scelta=int(input("inserisci 1, 2 o 3: "))
    while scelta>3 or scelta<0:
        scelta=int(input("inserisci 1, 2 o 3: "))
    if scelta==1:
        divisori(num)
    else:
        if scelta==2:
            potenza(num)
        else:
            primo(num)

def divisori(num):
    """
    parametri in ingresso:1
    parametri in uscita:1
    """
    conta=0 #quanti esponenti sono validi
    for div in range(1,num+1): #parte da 1 perchè altrimenti darebbe errore provando a dividere per 0
        if(num%div == 0):#controlla tutti i numeri se sono divisori
            conta += 1
    print("I divisori sono: ",conta)



def potenza(num):
    """
    parametri in ingresso: 1
    parametri in uscita:1
    """
    e=int(input("inserire l'esponente: "))
    ris= num**e
    print("il tuo numero è: ", ris)

def primo(num):
    """
    parametri in ingresso: 1
    parametri in uscita:1
    """
    if num % 2 == 0: #se il resto è 0 è pari
        print("Il numero è primo")
    else:
        print("Il numero non è primo")

#main
num=int(input("inserire numero intero: "))
menu(num)

        