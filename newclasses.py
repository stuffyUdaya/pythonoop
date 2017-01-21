from humangame import Human
class Wizard(Human):
    def __init__(self):
        super(Wizard,self). __init__()
        self.intelligence +=10
    def heal(self):
        self.health = self.health+10
class Ninja(Human):
    def steal(self):
        self.stealth = self.stealth+5
class Samurai(Human):
    def sacrifice(self):
        self.health = self.health-5
harry = Wizard()
rain = Ninja()
tom = Samurai()
print harry.health
print harry.intelligence
print rain.health
print tom.health
harry.heal()
print harry.health
rain.steal()
print rain.stealth
tom.sacrifice()
print tom.health
print tom.stealth
