import random

def dueDadi():
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    return dado1, dado2

#programma principale
print("lancio di due dadi")
volte = eval (input("inserisci nr. dati: "))
for n in range(0, volte):                          # n volte
    print(n+1,": ->",dueDadi() )                  #lancio casuale
#fine ciclo for
