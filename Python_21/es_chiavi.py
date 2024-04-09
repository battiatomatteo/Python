

def menu():
    """
    """
    chiavi=carica_chiavi()
    dizionario=carica_dizio(chiavi)
    print(dizionario)

def carica_chiavi():
    chiavi=[]
    x=int(input("Inserire num chiavi: "))
    for i in range(x):
        chiave=input("Inserire la chiave: ")
        chiavi.append(chiave)
    b=len(chiavi)
    chiavi=set(chiavi)
    c=len(chiavi)
    while c!=b:     
        diff=b-c
        for i in range(diff):
            chiave=input("Inserire la chiave: ")
            chiavi.add(chiave)
        c=len(chiavi)
    return chiavi

def carica_dizio(c):
    dizio={}
    c=list(c)
    x=len(c)
    for i in range(x):
        valore=int(input("Inserire il valore da assegnare alla chiave: "))
        a=c[i]
        dizio[a]=valore
    return dizio

#main
menu()