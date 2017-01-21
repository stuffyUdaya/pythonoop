class Car(object):
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

    def tax(self):
        if self.price >10000:
            tax = .15
            return tax
        else:
            tax =.12
            return tax
    def display(self):
        print "price",self.price
        print "speed",self.speed
        print "fuel",self.fuel
        print "mileage",self.mileage
        print "tax",self.tax()

car1 = Car(2000,'35mph','Full','15mpg')
car2 = Car(2000,'5mph','NotFull','105mpg')
car3 = Car(2000,'15mph','Kind of Full','95mpg')
car4 = Car(2000,'35mph','Full','25mpg')
car5 = Car(2000,'35mph','Empty','25mpg')
car6 = Car(12000,'35mph','Empty','15mpg')
car2.display()
