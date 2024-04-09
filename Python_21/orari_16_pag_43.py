#corretteza orari in ingresso in 3 input : h,m e s
print("inserisci ore,minuti e secondi")
ore = int(input())
min = int(input())
sec = int(input())

if ore > 0 and ore <= 24 :
    print("le ore sono corrette,", end = " ")
else :
    print("le ore non sono corrette,", end = " ")
if min > 0 and min <= 60 :
    print("i minuti sono corretti", end = " ")
else :
    print("i minuti non sono corretti", end = " ")
if sec > 0 and sec <= 60 :
    print("e i secondi sono corretti")
else :
    print("e i secondi non sono corretti")