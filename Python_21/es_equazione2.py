#Soluzione equazione di secondo grado 
#Forma canonica ax^2 + bx + c = 0
# 1) calcolo del delta b*b - 4*a*c
# 2) stampa soluzione 1mo grado nel caso a=0
# 3) stampa soluzione delta > 0 o == 0


def delta(a, b, c):
    """
    In questa funzione si calcola il delta 
    della nostra equazione mettendo in ingresso 
    tutti i coefficenti
    """
    delta = b * b - 4 * a * c
    return delta


def primo_grado(b, c):
    """
    Soluzione dell'equazione quando l'incognita alla seconda
    è uguale a 0 
    """
    if b == 0 and c == 0:
        print("Equazione indeterminata (presenta infinite soluzioni)")
    else:
        if b == 0:
            print("Equazione impossibile")
        else:
            print("x = ", -b/c)


def secondo_grado(a, b, c):
    """
    In questa funzione si risolve l'equazione quando si hanno 
    tutti i termini diversi da 0
    """
    deltae = delta(a, b, c)
    if delta == 0:
        print("x1 = x2 = ", -b/ ( 2 * a ))
    else:
        if deltae < 0:
            print("Equazione impossibile dato che il delta è minore di 0")
        else:
            print("x1 = ", (-b + pow(deltae, 1/2)) / (2 * a)    )
            print("x2 = ", (-b - pow(deltae, 1/2)) / (2 * a)    )





#main program
print("Risoluzione equazione di secondo grado")
a  = float(input("Inserire il coefficente dell'incognita alla seconda:  "))
b = float(input("Inserire il coefficente dell'incognita di primo grado:  "))
c = float(input("Inserire il coeffucente c:  "))

#condizioni per capire il caso
if a == 0:
    primo_grado(b, c)
else:
    secondo_grado(a, b, c)