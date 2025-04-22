class Zmogus:

    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __str__(self):
        return f"{self.vardas} {self.amzius} metų."

    def __repr__(self):
        return f"{self.vardas} {self.amzius} metų."
