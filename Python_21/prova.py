#dati di input due orari in ore, min e secondi
#visualizza la differenza in ore minuti e secondi


   
def differenza(h1, m1, s1, h2, m2, s2):
    """
    calcolo i secondi totali dei due orari dopo 
    faccio una sottrazione controllando qual'è l'orario 
    maggiore.
    parametri in ingresso: ora, minuti, secindi di entrambe le ore
    parametri in uscita: nessuno 
    """
    diff = ((h1 * 3600) + (m1 * 60) + s1) - ((h2 * 3600) + (m2 * 60) + s2)

    h1 = diff / 3600
    m1 = (diff - h1 * 3600)/ 60
    s1 = (diff - h1 * 3600) - (m1 * 60)

    print("la differenza è: ", h1, "ore", m1, "minuti", s1, "secondi")



#main program
h1=int(input("inserisci l'ora del primo orario: "))
m1=int(input("inserire i minuti del primo orario: "))
s1=int(input("inserire i secondi del primo orario: "))
h2=int(input("inserisci l'ora del secondo orario: "))
m2=int(input("inserire i minuti del secondo orario: "))
s2=int(input("inserire i secondi del secondo orario: "))


#chiamata funzione 
differenza(h1, m1, s1, h2, m2, s2)