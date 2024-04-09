#calcola in costo del biglietto di diverse autovetture e cilindrate
print("inserisci 1 se hai un auto e 2 se hai un camion")
vettura = int(input())
if vettura == 1 :
    print("seleziona 1 se è fino a 1000 cilindrata,2 se è fino a 2000 o 3 se è oltre")
    cc = int(input())
    if cc == 1 :
        print("il costo del biglietto è 20 euro")
    elif cc == 2 :
        print("il costo del biglietto è 30 euro")
    elif cc == 3 :
        print("il costo del biglietto è 40 euro")
    else :
        print("il numero inserito è errato,rifare")

elif vettura == 2 :
    print("seleziona 1 se è fino a 2000 cilindrata,2 se è fino a 3000 o 3 se è oltre")
    cc = int(input())
    if cc == 1 :
        print("il costo del biglietto è 40 euro")
    elif cc == 2 :
        print("il costo del biglietto è 50 euro")
    elif cc == 3 :
        print("il costo del biglietto è 100 euro")
    else :
        print("il numero inserito è errato,rifare")