import random

matrice=[
          []*6,
          []*6,
          []*6,
          []*6 
        ]

for y in range(4):
    for i in range(6):
        num=(int(random.randint(10, 100)))
        matrice[y][i]=num

print(matrice)


        

