print("inserire il primo voto")
voto1 = int(input())
print("inserire il secondo voto voto")
voto2 = int(input())
print("inserire il terzo voto")
voto3 = int(input())
totvoti = voto1 + voto2 + voto3
media = float(totvoti) / 3
if media < 3:
    print("il voto è nullo")
else:
    if (3 <= media) <= 4.5:
        print("La media dei voti è gravemente insufficiente")
    else:
        if (4.5 <= media) <= 6:
            print("La media dei voti è insufficiente sufficiente")
        else:
            if (6 <= media) <= 7.5:
                print("La sua media è sufficiente")
            else:
                if (7.5 <= media) <= 9:
                    print("La sua media è buona, complimenti")
                else:
                    if media > 9:
                        print("La sua media è eccellente, complimenti")