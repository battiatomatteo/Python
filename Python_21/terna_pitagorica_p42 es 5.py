#dati 3 numeri scrivi se formano una terna petagorica
print("inserisci 3 numeri")
a = int(input())
b = int(input())
c = int(input())

if a**2 + b**2 == c**2 :
    print("i numeri inseriti formano una terna pitagorica")
else :
    print("i numeri inseriti NON formano una terna pitagorica")