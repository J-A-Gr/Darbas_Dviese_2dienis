from file_reader import FileReader
from klase_zmogus import Zmogus


sarasas = []


# Funkcija už klasės ribų
def ivestis_zmogaus():
    vardas = input("Įveskite savo vardą: ")
    amzius = input("Įveskite savo amžių: ")

    sarasas.append(Zmogus(vardas, amzius))  # Pridedam į klasės sąrašą
    print("Žmogus sėkmingai pridėtas!")

# Naudojimas:
ivestis_zmogaus()

print(sarasas)

for zmogus in sarasas:
    print(zmogus)

# Save content
FileReader.save_to_file("zmoniu_sarasas.txt", sarasas)

# Read content
zmoniu_sarasas = FileReader.read_from_file("zmoniu_sarasas.txt")
print(zmoniu_sarasas)


def skaiciuoti_vidurki_is_failo(filename):
    turinys = FileReader.read_from_file(filename)
    eilutes = turinys.strip().split("\n")
    
    amziai = []
    for eilute in eilutes:
        try:
            # Tavo formatas: "Linas 29 metų."
            dalys = eilute.strip().split()  # padalina pagal tarpelius
            amzius = int(dalys[1])  # antras elementas yra amžius
            amziai.append(amzius)
        except (IndexError, ValueError):
            print(f"Klaida apdorojant eilutę: '{eilute}'")
    
    if amziai:
        vidurkis = sum(amziai) / len(amziai)
        print(f"Amžiaus vidurkis: {vidurkis:.2f} metų")
    else:
        print("Nėra amžių duomenų skaičiavimui.")

# Kvietimas:
skaiciuoti_vidurki_is_failo("zmoniu_sarasas.txt")

