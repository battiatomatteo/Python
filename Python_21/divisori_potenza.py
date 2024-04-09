def seleziona():
    """è il menu"""
    print("Scrivi 1 per visualizzare i divisori \nScrivi 2 per elevare alla potenza \nScrivi 3 per verificare se si tratta di un numero primo")
    comando = int(input())
    while comando > 3 or comando < 0: #controllo
        comando = int(input("Riscrivi un comando tra quelli proposti: "))
    if comando == 1: #richiama i comandi scelti
        numdiv(num)
    elif comando == 2:
        potenza(num)
    else:
        verifica(num)

def numdiv(num):
    """ conta i divisori
    paramentri in ingresso : num"""
    conta=0 #quanti esponenti sono validi
    for div in range(1,num+1): #parte da 1 perchè altrimenti darebbe errore provando a dividere per 0
        if(num%div == 0):#controlla tutti i numeri se sono divisori
            conta += 1
    print("I divisori sono: ",conta)



def potenza(num):
    """eleva una potenza
    parametri in ingresso : num"""
    esp = int(input("Scrivi l'esponente a cui elevare: "))
    ris = num ** esp #esegue la potenza
    print(str(ris))

def verifica(num):
    """verifica se il numero è primo
    parametri in ingresso : num"""
    if num % 2 == 0: #se il resto è 0 è pari
        print("Il numero è primo")
    else:
        print("Il numero non è primo")

#MAIN
num = eval(input("Inserisci un numero: "))
seleziona()