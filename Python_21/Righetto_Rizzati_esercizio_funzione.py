def prodotti_forn(dizionario):
    """stampa a video tutti i prodotti di un fornitore dato in input
    P.in ingresso : dizionario dal main
    
    Programmato da Righetto Giacomo e Rizzati Riccardo"""
    forn=input("Inserire il nome del fornitore di cui si vogliono sapere i prodotti: ")
    prod=[] #lista in cui inserire i prodotti
    for i in dizionario: #scorro gli elementi del dizionario
        if forn in dizionario[i]["Fornitore"]: #per ogni elemento cerco nella chiame "Fornitore"
            prod.append(dizionario[i]["Descrizione"])

    if len(prod) == 0: #controllo se ci sono prodotti
        print("Non si dispone di alcun prodotto da questo fornitore")
    else:
        print("I prodotti del fornitore richiesto sono:",prod)

#MAIN (esempio dizionario del main)
dizio={1000:{"Descrizione":"mela","Reparto":"frutta","Fornitore":"De Carli","Giacenza":1,"Quantità minima":5},
10001:{"Descrizione":"Banana","Reparto":"frutta","Fornitore":"De Carli","Giacenza":1,"Quantità minima":5},
10002:{"Descrizione":"Arancia","Reparto":"frutta","Fornitore":"Da Carlo","Giacenza":1,"Quantità minima":5}
}

prodotti_forn(dizio)
