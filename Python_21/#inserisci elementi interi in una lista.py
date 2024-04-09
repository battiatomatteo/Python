#inserisci elementi interi in una lista
"""
mi crea una lista vuota
"""
lista=[]
x=int(input("inserire grandezza lista: "))
for i in range(x):
    num=int(input("inserire un numero: "))
    lista.append(num)
print(lista)