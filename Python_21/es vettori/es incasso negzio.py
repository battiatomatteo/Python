#Calcolare l'icasso settimanale di un negozio dopo aver letto e memorizzato in una lista (vettore) l'incasso giornaliero.

vettore = [0] * (7)

incassotot = 0
x = 0
for g in range(1, 7 + 1, 1):
    print("incasso giornaliero")
    incasso = int(input())
    vettore[x] = incasso
    x = x + 1
    incassotot = incassotot + incasso
