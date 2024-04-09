#stabilire quanti e quali attrezzi mancano a mario gianni e franco,
#ogni persona neccessita di un set diverso di attrezzi
#io devo vedere se mario gianni e franco hanno i loro set
#altrimenti scrivere quali mancano e quanti sono

def controllo(pers,attrezzitotali):
    """
    controlla se mancano degli attrezzi
    P.in ingresso : Attrezzi delle persone
    """
    if pers == attrezzitotali:
        print("Ha tutti gli attrezzi")
    else:
        mancanti = attrezzitotali.difference(pers)
        print("Gli mancano :",mancanti,"\n")

def stampa(attrezzitotali,attrezziM,attrezziG,attrezziF):
    """
    stampa i risultati di controllo
    """
    print("Ora controlleremo Mario")
    controllo(attrezziM,attrezzitotali)
    print("Ora controlleremo Gianni")
    controllo(attrezziG,attrezzitotali)
    print("Ora controlleremo Franco")
    controllo(attrezziF,attrezzitotali)

#main
attrezzitotali = {"martello, trapano, cacciavite, pinze, viti, chiodi, forbici"}
attrezziM = {"pinze, cacciavite, viti"}
attrezziG = {"trapano, martello, chiodi"}
attrezziF = {"cacciavite, pinze, forbici"}
stampa(attrezzitotali,attrezziM,attrezziG,attrezziF)