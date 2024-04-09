
def main():
    """
    P.ingresso://
    P.uscita://
    """
    n1=int(input("Inserire un numero: "))
    n2=int(input("Inserire un numero: "))
    n=0
    print(div(n1, n2, n))

def div(num1, num2, ris):
    """
    P.ingresso:num1, num2, ris
    P.uscita:ris
    """
    if num1 >= num2:
        num1=num1-num2
        ris=div(num1, num2, ris)+1        
    return ris

#main
main()