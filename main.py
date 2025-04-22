from file_reader import FileReader
from klase_zmogus import Zmogus
from skaiciuoti_vidurki import skaiciuoti_vidurki_is_failo


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

# Kvietimas:
skaiciuoti_vidurki_is_failo("zmoniu_sarasas.txt")

