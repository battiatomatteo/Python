#inseriti 2 numeri, dire se il secondo è un divisore del primo

def divisori(a,b):
    if a % b == 0:
        print("il secondo numero è divisore del primo")
    else :
        print("il secondo numero non è un divisore del primo")

#main program
a=int(input("inserire il primo numero: "))
b=int(input("inserire secondo numero: "))

divisori(a, b)