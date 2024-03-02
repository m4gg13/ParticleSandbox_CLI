class Molecule:
    def __init__(self):
        self.type = "molecule"

class HydrogenGas(Molecule):
    def __init__(self, number):
        super().__init__()
        self.number = number

class Ammonia(Molecule):
    def __init__(self, number):
        super().__init__()
        self.number = number
