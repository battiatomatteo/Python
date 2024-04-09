#calcola il quadrato di un numero inserito
#usare le funzioni

def calcola_quadrato(num):
    quadrato=num*num
    return quadrato


#main program
num=int(input("inserire un numero: "))

mario=calcola_quadrato(num)
print("il quadrato del tuo numero è: ", mario)