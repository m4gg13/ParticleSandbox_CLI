class Matter:
    def __init__(self):
        self.type = "matter" # can be `matter`, `particle`, `atom`, `molecule`

class Describable:
    def __init_(self):
        self.number = 0
    def describe():
        return ""

class Coordinates(Describable):
    def __init_(self):
        super.__init_()
        self.x = 0
        self.y = 0
        self.z = 0
    def describe(self):
        description = str(self.x) + " "
        description += str(self.y) + " "
        description += str(self.z)
        return description
