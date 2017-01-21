class Animal(object):
    def __init__(self,name):
        print "new animal added"
        self.name =name
        self.health = 100

    def walk(self):
        self.health -=1
        return self
    def run(self):
        self.health -=5
        return self
    def displayHealth(self):
        print "Animal's name:" +str(self.name)
        print "Animal's health:" +str(self.health)
        return self



# animal = Animal("Dog")
# animal.walk().walk().walk().run().run().displayHealth()
