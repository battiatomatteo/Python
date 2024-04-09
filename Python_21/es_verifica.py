def esponente():
    """
    parametri in ingresso: 0
    parametri in uscuta: 1
    """
    esp=int(input("inserire l'esponente del tuo numero: "))
    return esp

def base():
    """
    parametri in ingresso: 0
    parametri in uscuta:1
    """
    bs=int(input("inserire la base del tuo numero: "))
    return bs

def calcolo(e, b):
    """
    parametri in ingresso:2
    parametri in uscita: 1
    """
    ris=b**e
    return ris
    
#main
e=esponente()
b=base()
c=calcolo(e, b)
print("il tuo numero è: ", c)




