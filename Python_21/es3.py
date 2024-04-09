# Dati N numeri determinare il maggiore, il minore e la differenza tra i due.
n = int(input())
num = int(input())
prec = 0
minore = num
maggiore = num
for v in range(1, n + 1, 1):
    if num > prec:
        maggiore = num
        minore = prec
    else:
        maggiore = prec
        minore = num
    num = int(input())
diff = maggiore - minore
print(diff)
print(maggiore)
print(minore)
