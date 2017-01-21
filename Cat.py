# class Cat(object):
#     pass
# garfield = Cat()
# garfield.color = "orange"
# garfield.type = "fat"
# garfield.age = 5
# print "Garfield's color:", garfield.color
# print "Garfield's type:", garfield.type
# print "Garfield's age:", garfield.age



class Cat(object):
    def __init__(self,color,type,age):
        self.color = color
        self.type = type
        self.age = age
garfield = Cat('Orange','Lean',10)
print "Garfield's Color:", garfield.color
print "Garfield's type:", garfield.type
print "Garfield's age:", garfield.age
