class Matter:
    def __init__(self):
        self.type = "matter" # can be `matter`, `particle`, `atom`, `molecule`

class Coordinates():
    def __init__(self, x:float, y:float, z:float):
        print('COORD++==')
        print(float(x))
        print(float(y))
        print(float(z))
        self.x:float = float(x)
        self.y:float = float(y)
        self.z:float = float(z)
    def describe(self):
        description = str(self.x) + " "
        description += str(self.y) + " "
        description += str(self.z)
        return description
