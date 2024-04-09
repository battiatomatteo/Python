#inserisci i voti di una classe di informatica
#visualizzare le medie di ciascun alunno


def media_voti():
    for v in range(1, alunni + 1, 1):
        nverifiche = int(input("inserire numero di verifiche svolte dall'alunno"))
        totverifiche = 0

        for i in range(1, nverifiche + 1, 1):                   
            voto = int(input("inserire voto della verifica"))   
            totverifiche = voto + totverifiche

        media = float(totverifiche) / nverifiche
        print(media)

      


#programma principale
alunni = int(input("inserire numero allunni di informatica"))
if alunni<=0:                                #controllare se il numero degli alunni è corretto 
    while alunni<=0:
        alunni=int(input("reinserire numero alunni"))
                                            #non bisogna reinserire il numero di alunni
else:
    pass

#chiamata funzione
media_voti()
