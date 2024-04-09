#scrivi un programma che visualizza in ordine decrescente i numeri naturali da 0a N
N=int(input("num di partenza"))
N2=int(input("num finale"))
for num in range(N, N2 - 1,-1):
    print(num)
