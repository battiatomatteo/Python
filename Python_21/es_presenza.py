#creare un programma per gestire magazzino e negozio di ortofrutta.
#1)visualizzare l'insieme degli ortaggicpresenti in magazzino e in negozio.
#2)visualizzare lista degli ortaggi che devono essere recuperati dal magazzino perchè terminati in negozio.
#3)visualizzare elenco degli ortaggi che sono terminati in negozio e devono essere riodinati.

def main():
    """
    P.ingresso://
    P.uscita:
    """
    print("Prima")
    negozio={"insalata", "pomodori", "patate", "banana", "anguria"}
    magazzino={"patate", "banana", "anguria", "ciliegie", "mandarini", "fragole"}
    ordini={"insalata", "pomodori", "patate", "banana", "anguria", "ciliegie", "mandarini", "fragole", "cocomeri", "melanzane"}
    print(negozio,"\n", magazzino, "\n", ordini)
    print("\nDopo")
    tutti=unione(negozio, magazzino)
    print("Questi sono tutti gli oggetti presenti nel magazzino e negozio:")
    print(tutti, "\n")
    rec=recuperati(negozio, magazzino)
    print("Questi sono gli oggetti da recuperare dal mgazzino:")
    print(rec, "\n")
    man=mancanti(tutti,ordini)
    print("Questi sono gli oggetti che mi mancano:")
    print(man, "\n")
    rimozione(tutti)

def unione(a,b):
    """
    Unione dei due  insiemi
    P.ingresso:a,b
    P.uscita:tutti
    """
    tutti=a.union(b)
    return tutti
    

def recuperati(a,b):
    """
    visualizzare lista degli ortaggi che devono essere recuperati dal magazzino
    perchè terminati in negozio.
    P.ingresso:a,b
    P.uscita:rec
    """
    rec=b.difference(a)
    rec=list(rec)
    return rec
   
def mancanti(a,b):
    """
    visualizzare elenco degli ortaggi che sono terminati in negozio e devono essere riodinati.
    P.ingresso:a,b
    P.uscita:ma
    """
    ma=b.difference(a)
    sorted(ma)
    return ma

def rimozione(insieme):
    """
    P. ingresso: insieme
    P. uscita://
    """
    print("Prima", insieme)
    elemento=input("Inserire elemento da togliere: ")
    if elemento in insieme:
        insieme.remove(elemento)
    else:
        print("Elemento non presente")
    print("Dopo\n",insieme)

#main
main()