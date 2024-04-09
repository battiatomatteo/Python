global num1
global num2

def funzione1():
    global num1
    num1 = num1 + 11
    num2 = 12
    return

def funzione2():
    global num2
    num1 = 20
    num2 = num2 + 22
    return

# programma principale
print("Le regole di visibilità")
num1 = 100
num2 = 200
print("num1 ", num1, " num2 ", num2)
funzione1()
print("num1 ", num1, " num2 ", num2)
funzione2()
print("num1 ", num1, " num2 ", num2)
