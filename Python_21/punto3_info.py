def ordine_alfa( nomi, classi):
    """
    visualizzare, suddivisi per classe-sezione, tutti gli studenti ordinando per nominativo
    P.ingresso:nomi, classi
    P.uscita://
    """
    if len(nomi[0]) ==0:    #controllo se nomi è vuoto
       print("inserisci prima i nomi")
    else:                         
        for a in range(len(nomi)):
            print(classi[a])    #stampo a video la classe (es: "1A")
            lista=[]        #creo una lista dove inserire i nomi e cognomi 
            for key in nomi[a]:
                b=nomi[a][key]["Cognome nome"]  #scorro la lista di dizio
                lista.append(b)     #inserisco nella lista la variabile b
            lista=sorted(lista)     #assegno alla variabile lista una lista ordinata
            print(lista)    #stampo a video la lista ordinata


