class Particle:
    def __init__(self, number, mass, coordinate):
        self.number = number
        self.mass = mass
        self.coordinate = coordinate
        self.name = "generic"
        self.type = "particle"

class Fermion(Particle):
    def __init__(self, number):
        super().__init__(number, 1, 1)
        self.fundamental_class = ["fermion"]
        self.interactions = ["strong", "weak", "electromagnetic", "gravity"]

class UpQuark(Fermion):
    def __init__(self, number):
        super().__init__(number)
        self.number = number
        self.coordinate = 1
        self.name = "up"
        self.symbol = "u"
        self.spin = 0.5
        self.charge = 2/3
        self.mass = 2.2 * 10**6
        self.generation = 1
        self.family = "quark"
        self.decay_product = {
            "stable":0,
            "down":1,
            "positron":1,
            "electron neutrino":1
        }

class DownQuark(Fermion):
    def __init__(self, number):
        super().__init__(number)
        self.number = number
        self.coordinate = 1
        self.name = "down"
        self.symbol = "d"
        self.spin = 0.5
        self.charge = -1/3
        self.mass = 4.7 * 10**6
        self.generation = 1
        self.family = "quark"
        self.decay_product = {
            "stable":0,
            "up":1,
            "electron":1,
            "electron antineutrino":1
         }

class Proton:
    def __init__(self, number):
        super().__init__(number)
        self.number = number
        self.coordinate = 1
        self.name = "proton"
        self.spin = 0.5
        self.charge = 1
        self.mass = 938.272 * 10**6


# notes
# mass is measured in electron volts per speed of light squared
# so a mass * 10**6 means Mega electron volts per speed of light squared
# `fundamental_class` - can be `fermion`, 'boson', and `hadron`
#
# according to https://en.wikipedia.org/wiki/Up_quark
# up quarks decay into stable or down quark + positron + electron neutrino
#
#
