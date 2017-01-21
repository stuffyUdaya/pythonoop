from Animal import Animal
class Dragon(Animal):
    def __init__(self,name):
        print "Dragon added"
        super (Dragon,self). __init__(name)
        self.health =170
    def fly(self):
        self.health -=10
        return self
    def display(self):
        print "this is a dragon!"
        self.displayHealth()
        return self
dragon = Dragon("Danerys")
dragon.walk().walk().walk().run().run().fly().fly().display()
