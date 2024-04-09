#scrivere un programma che acquisisca numeri interi in input e li aggiunga a una lista, se non sono già presenti al suo interno. 
#Terminare l'inserimento quando la lista contiene 10 valori e visualizzare gli elementi.

lista = []
for i in range(10):
    numero = int(input("Inserisci un numero:  "))
    if i == 0:
        lista.append(numero)
    else:
        for a in range(len(lista)):
            c = lista.count(numero)     #count=conta quante volte è presente un valore dentro una lista
            if c == 1:
                break   #stoppa il ciclo
        if c == 1:
            print("Il numero è già presente nella lista, non è stato inserito.")
            i = i - 1
        else:
            lista.append(numero)

#main program
print(lista)
