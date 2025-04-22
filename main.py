from file_reader import FileReader
from klase_zmogus import Zmogus
import os

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

# Skaičiuojam vidutinį amžių
if sarasas:
    vid_amzius = sum(z.amzius for z in sarasas) / len(sarasas)
    print(f"\nVidutinis amžius: {vid_amzius:.1f} m.")
else:
    print("\nSąrašas tuščias – nėra ką skaičiuoti.")
