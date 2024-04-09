def n_cifre(num):
    """
    """
    cifre=0
    if num>0:
        num=num//10  
        cifre=n_cifre(num)+1
    return cifre

def main():
    num=int(input("Inserire un numero: "))
    print(n_cifre(num))

#main
main()


