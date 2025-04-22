class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = int(amzius)

    def __repr__(self):
        return f"{self.vardas}, {self.amzius} m."