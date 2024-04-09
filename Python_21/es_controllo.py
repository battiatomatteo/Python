#scrivere il codice per inserire un numero in una lista se in questa lista è presente un numero negativo (sostituirlo)

def lista():
    
    x=int(input("Quanti numeri desideri inserire nella lista? "))
    for i in range(x):
        num=int(input("Inserire un numero: "))
        lista.append(num)
    print(lista)
    lista.append(-3)
    return lista

def controllo():
    for i in range(len(llista)):
        if lista[i]<0:
            num=int(input("Inserire un numero positivo: "))
            lista[i]=num
    print(lista)
    return lista

#main
lista[0]
c=controllo()
l=lista()
print(c)
print(l)

"""
lista[]
x=int(input("Quanti numeri desideri inserire nella lista? "))
for i in range(x):
    lista.append(int(input("Inserire un numero: ")))
print(lista)
lista.append(-3)

for i in range(len(llista)):
    if (lista[])
    while (lista[i]<0):
        num=int(input("Inserire un numero positivo: "))
        lista[i]=num
print(lista)
"""

"""
lista=[]
x=int(input("Quanti numeri desideri inserire nella lista? "))
for i in range(x):
    num=int(input("Inserire un numero: "))
    while num<0:
        num=int(input("Inserire un numero positivo: "))
    lista.append(num)
print(lista)
""" 