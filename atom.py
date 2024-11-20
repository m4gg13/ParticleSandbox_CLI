class Atom:
    def __init__(self):
        self.type = "atom"
        import matter
        # TODO collect the proper coordinates
        self.coordinates = matter.Coordinates(0, 1, 2)
        # self.coordinates = matter.Coordinates()

class Hydrogen(Atom):
    def __init__(self, number):
        super().__init__()
        self.name = "hydrogen"
        self.symbol = "H"
        self.number = number
        self.electrons = 2
        self.protons = 2
        self.neutrons = 2
        self.energy_initial = 1
        self.energy_final = 1
        self.spin = 1
