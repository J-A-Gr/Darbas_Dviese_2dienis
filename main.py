from file_reader import FileReader
from klase_zmogus import Zmogus
import os
from skaiciuoti_vidurki import skaiciuoti_vidurki_is_failo

# Nuskaityk esamus žmones, jei failas egzistuoja
if os.path.exists("zmoniu_sarasas.pkl"):
    sarasas = FileReader.read_from_file("zmoniu_sarasas.pkl")
else:
    sarasas = []

# Funkcija už klasės ribų
def ivestis_zmogaus():
    vardas = input("Įveskite savo vardą: ")
    amzius = input("Įveskite savo amžių: ")
    sarasas.append(Zmogus(vardas, int(amzius)))  # užtikrink, kad amžius būtų skaičius
    print("Žmogus sėkmingai pridėtas!")

# Įvestis ir saugojimas
ivestis_zmogaus()

# Išsaugom atnaujintą sąrašą į failą
FileReader.save_to_file("zmoniu_sarasas.pkl", sarasas)

# Atvaizduojam visus žmones
print("\nŽmonių sąrašas:")
for zmogus in sarasas:
    print(zmogus)

# Save content
FileReader.save_to_file("zmoniu_sarasas.txt", sarasas)

# Read content
zmoniu_sarasas = FileReader.read_from_file("zmoniu_sarasas.txt")
print(zmoniu_sarasas)

# Kvietimas:
skaiciuoti_vidurki_is_failo("zmoniu_sarasas.txt")

