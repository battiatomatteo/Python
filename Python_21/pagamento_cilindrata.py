# scirvere un programma per sapere quanto bisogna pagare in base alla cilindrata dell'autovettura e camion.

autovetture = int(input())
camion = int(input())
cilindrata = 0

# determiniamo quanto pagare in abse alla cilindrata dell 'auto

if autovetture <= 1000:
    print("paghi 20")
else:
    if autovetture <= 2000:
        print("paghi 30")
    else:
        if autovetture > 2000:
            print("paghi 40")
        

# ora invece determiniamo quanto pagare in base alla cilindrata del camion.
if camion <= 2000:
    print("paghi 40")
else:
    if camion <= 3000:
        print("paghi 50")
    else:
        if camion > 3000:
            print("paghi 100")
