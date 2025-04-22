from file_reader import FileReader

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