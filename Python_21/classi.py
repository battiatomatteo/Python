#classi

class Persona:
    def __init__(self, nome, cognome, residenza):
        self.nome = nome
        self.cognome = cognome
        self.residenza = residenza

    def scheda(self):
        return f"Nome: {self.nome}\nCognome:{self.cognome}\nResidenza:{self.residenza}"

class Studente(Persona):
    def __init__(self, nome, cognome, residenza, corso):
        super().__init__(nome, cognome, residenza)
        self.corso= corso

    def scheda(self):
        scheda = f"\nCorso: {self.corso}"
        return super().scheda() + scheda

class Insegnante(Persona):
    def __init__(self, nome, cognome, residenza, materie):
        super().__init__(nome, cognome, residenza)
        if materie is None:
            self.materie = []
        else:
            self.materie = materie
    def scheda(self):
        s = f"\nMateria insegnante: {self.materia}"
        return super().scheda() + s

def studente():
    nome=input("Inserire nome: ")
    cognome=input("Inserire cognome: ")
    residenza=input("Inserire residenza: ")
    materia=input("Inseire materia: ")
    return nome, cognome, residenza, materia

def insegnante():
    nome=input("Inserire nome: ")
    cognome=input("Inserire cognome: ")
    residenza=input("Inserire residenza: ")
    materia=input("Inseire materia: ")
    return nome, cognome, residenza, materia

#main
#studente = Studente("Matteo", "Battiato", "Caldiero", "Informatica e Telecomunicazione")
#print(studente.scheda())

for i in range(2):
    print("""
    MENU
    1)Studente
    2)Insegnate
    """)
    scelta=int(input("Inserire scelta: "))
    if scelta==1:
        n, c, r, cs = studente()
        ragazzo = Studente(n, c, r, cs)
        print(ragazzo.scheda())
    else:
        n, c, r, mi = insegnante()
        insg= Insegnante(n, c, r, mi)
        print(insg.scheda())

