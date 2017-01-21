class Bike(object):
    def __init__(self,price,max_speed,miles=0):
        self.price=price
        self.miles=miles
        self.max_speed=max_speed
bike1= Bike(200,'250mph')
bike2 = Bike(400,'150mph')
bike3= Bike(700,'100mph')

def ride(x,y):
    for i in range(0,y):
        x.miles = x.miles+10
        print "riding:",x.miles
ride(bike1,3)
def reverse(x,y):
    for i in range(0,y):
        x.miles = x.miles-5
        print "Reversing:",x.miles
reverse(bike1,1)
def displayInfo(x):
    print "price of bike",(x.price)
    print "max-speed of bike",(x.max_speed)
    print "total miles driven on bike",(x.miles)
displayInfo(bike1)
def ride(x,y):
    for i in range(0,y):
        x.miles = x.miles+10
        print "riding:",x.miles
ride(bike2,2)
def reverse(x,y):
    for i in range(0,y):
        x.miles = x.miles-5
        print "Reversing:",x.miles
reverse(bike2,2)
def displayInfo(x):
    print "price of bike",(x.price)
    print "max-speed of bike",(x.max_speed)
    print "total miles driven on bike",(x.miles)
displayInfo(bike2)
def reverse(x,y):
    for i in range(0,y):
        if x.miles<=0:
            print "Miles are less than 0"
        else:x.miles = x.miles-5
        print "Reversing:",x.miles
reverse(bike3,3)




# print "Test 1 has phrase: "  % bike1.price

# def displayInfo(x):
#
#     print "bike price:",x.price
#     print "max-speed:",x.max_speed
#     print "totalmiles:",x.miles
# displayInfo('bike1')
