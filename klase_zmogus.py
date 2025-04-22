class Zmogus:
    human_list = []  # Klasės kintamasis

    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __str__(self):
        return f"{self.vardas} {self.amzius} metų."

    def __repr__(self):
        return f"{self.vardas} {self.amzius} metų."

# Funkcija už klasės ribų
def ivestis_zmogaus():
    vardas = input("Įveskite savo vardą: ")
    amzius = input("Įveskite savo amžių: ")

    zmogus = Zmogus(vardas, amzius)  # Kuriame Zmogus objektą
    Zmogus.human_list.append(zmogus)  # Pridedam į klasės sąrašą
    print("Žmogus sėkmingai pridėtas!")

# Naudojimas:
ivestis_zmogaus()
ivestis_zmogaus()

print(Zmogus.human_list)

for zmogus in Zmogus.human_list:
    print(zmogus)
