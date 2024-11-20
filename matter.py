class Matter:
    def __init__(self):
        self.type = "matter" # can be `matter`, `particle`, `atom`, `molecule`

class Coordinates():
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
    def describe(self):
        description = str(self.x) + " "
        description += str(self.y) + " "
        description += str(self.z)
        return description
