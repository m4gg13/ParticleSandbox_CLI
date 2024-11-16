class Matter:
    def __init__(self):
        self.type = "matter" # can be `matter`, `particle`, `atom`, `molecule`

class Describable:
    def __init_(self):
        self.number = 0
    def describe():
        return ""

# TODO why can this not take params????
class Coordinates():
    # def __init_(self):
    #     super().__init_()
    #     self.x = 1
    #     self.y = 1
    #     self.z = 1
    def __init_(self, x, y, z):
        # super().__init_()
        self.cx = x
        self.cy = y
        self.cz = z
    def describe(self):
        description = str(self.cx) + " "
        description += str(self.cy) + " "
        description += str(self.cz)
        return description
