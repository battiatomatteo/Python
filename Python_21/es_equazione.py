#Scrivere un programma che mi permetta di individuare se un equazione è di primo o secondo grado
#e calcolare i risultati in entrambi i casi, dati in input il valore dedlla a, della b, della c.

#definizione delle funzioni
def main():
    """
    L'utente inserisce i valori di a, b, c. Controlla se a è uguale a 0
    P. ingresso: //
    P. uscita: //
    """
    print("Soluzione euazione")
    a = float(input("Inserire a: "))
    b = float(input("Inserire b: "))
    c = float(input("Inserire c: "))

    #controllo grado equazione
    if(a == 0):
        primo_grado(b,c)
    else:
        soluzioni(a, b, c)

def primo_grado(b,c):
    """
    Calcola soluzione primo grado quando a = 0
    P. ingresso: 2
    P. uscita: //
    """
    if ((b == 0) & (c== 0)):
        print("Equazione di primo grado indeterminata(infinite soluzioni)")
    else:
        if (b == 0):
            print("Equazione impossibile!")
        else:
            print("x = ", -c/b)

def delta(a, b, c):
    """
    Calcolo del delta
    P. ingresso: 3
    P. uscita: 1
    """
    d = b*b - 4*a*c
    return d

def soluzioni(a, b, c):
    """
    Calcolo soluzioni con chiamata a Delta
    P. ingresso: 3
    P. uscita: //
    """
    deltac = delta(a, b, c)
    if (deltac < 0):
        print("Non esistono soluzioni reali")
    else:
        x1 = (-b+deltac**(1/2))/(2*a)
        x2 = (-b-deltac**(1/2)/(2*a))
        print("x1= ", x1," ", "x2= ", x2)
    return
                  
    
#main program
main()
