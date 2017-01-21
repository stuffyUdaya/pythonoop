class Bike1(object):
            def __init__(self,price,max_speed):
                self.price = price
                self.max_speed=max_speed
                self.miles = 0;
            def displayinfo(self):
                print 'price is: $'+ str(self.price)
                print 'Max Speed:' + str(self.max_speed) + 'mph'
                print 'Total Miles:' +str(self.miles) + 'miles'
                return self

            def ride(self):
                print'Driving'
                self.miles = self.miles+10
                return self
            def reverse(self):
                print 'reversing:'
                if self.miles>=5:
                    self.miles = self.miles-5
                return self

bike1 = Bike1(200,350)
bike1.ride().ride().reverse().displayinfo()
