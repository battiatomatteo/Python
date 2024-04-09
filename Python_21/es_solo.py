
#Creare un progamma che gestisce un magazzino di un negozio di ortofrutta, è presente un menù dove dice di inserire elementi presenti 
#in negozio e in magazzino,visualizzare quelli finiti, visualizzare tutti i prodotti, modificare o aggiungere un prodotto

def main():
    """
    """
    negozio=inserimento()
    print("Elementi presenti in negozio:\n", negozio)
    magazzino=inserimento()
    print("Elementi presenti in magazzino:\n", magazzino)
    tutti=t(negozio, magazzino)
    scelta=int(input("Inserire 1 se si vuole cambiare/aggiungere un elemento\n Inserire 0 se non si desidera cambiare/aggiungere un elemento\n"))
    while scelta<0 or scelta>1:
        scelta=int(input("Inserire 1 se si vuole cambiare/aggiungere un elemento\n Inserire 0 se non si desidera cambiare/aggiungere un elemento\n"))
    if scelta==1:
        modifica(tutti)

def inserimento():
    """
    """
    lista=[]
    x=int(input("Inserire quanti elementi si voglioni inserire nel magazzino."))
    for i in range(x):
        elemento=input("Inserire un elemento elemento")
        lista.append(elemento)
    return lista

def t(b,c):
    """
    """
    set(b)
    set(c)
    tutti=c.union(b)
    return tutti


def modifica(a):
    """
    """
    scelta=int(input("1 se si vuole togliere un elemento \n 0 se si vuole aggiungere:"))
    while scelta<0 or scelta>1:
        scelta=int(input("1 se si vuole togliere un elemento \n 0 se si vuole aggiungere:"))
    if scelta==0:
        elemento=input("Inserire elemento")
        a.add(elemento)
    else:
        elemento=input("Inserire elemento")
        if elemento in a:
            a.remove(elemento)
        else:
            print("Elemento non presente")
    print("Il tuo insieme è: ", a)

#main
main()