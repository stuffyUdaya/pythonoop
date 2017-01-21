import random
class Human(object):
    def __init__(self,clan=None):
        print "New Human added"
        self.health=100
        self.clan = clan
        self.strength = 3
        self.intelligence =3
        self.stealth =3
    def taunt(self):
        print "you want a piece of me?"
    def attack(self):
        self.taunt()
        luck = round(random.random()*100)
        if(luck>50):
            if(luck*self.strength>150):
                print "luck is " +str(luck)
                print 'attacking!'
                return True
            else:
                print "luck is:" +str(luck)
                print 'attack failed!!'
                return False
        else:
                self.health = self.health=self.strength
                print "attack failed!!"
                print "heath is: "+str(self.health)
                return False
# human1 = Human('wizard')
# human2 = Human()
# human2.attack()
