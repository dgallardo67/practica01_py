class Dog :
    def __init__(self, name, size, colour, race):
        self.name = name
        self.size = size
        self.colour = colour
        self.race = race
    def printinfo(self) :
        print(self.name, self.size, self.colour, self.race)

dog = Dog("Parches", 60, "bicolor", "dalmata incomprendido")

dog.printinfo()
