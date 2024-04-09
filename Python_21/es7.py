#Calcolare la somma dei primi dieci numeri interi successivi a un numero N.
n = int(input())
somma = n
sommas = 0
for v in range(1, 10 + 1, 1):
    somma = somma +1
    somma = somma + sommas
print(sommas)    
