#Scrivi una funzione che, a scelta dell'utente, calcoli l'area di:
#un cerchio
#un quadrato
#un rettangolo
#un triangolo
#Sentiti libero/a di estendere le potenzialità della funzione quanto meglio credi...

def figura():
    """
    parametri in ingresso: 0
    parametri in uscita: 1
    """
    f=str(input("inserire il tipo di figura: "))
    return f

def tipo_calcolo(lato, f):
    """
    parametri in ingresso: 2
    parametri in uscita: 1
    """
    if f=="quadrato":
        area = num*num
    else:
        if f=="rettangolo":
            num2=int(input("inserire altezza del rettangolo: "))
            area = num * num2
        else:
            if f=="triangolo":
                num2=int(input("inserire altezza del triangolo: "))
                area = num * num2
            else:
                area = (num * num) * 3,14
    return area


#main program
f=figura()
num=int(input("inserire la misura del lato: "))
a=tipo_calcolo(num, f)
print("l'area della figura è: ", a)