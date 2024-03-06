#class Animal():
#    def __init__(self):
#        print("Animal created")
#    def whoAmI(self):
#        print("ANIMAL")
#    def eat(self):
#        print('EATING')
#mya =Animal()
#mya.whoAmI()
#mya.eat()            

class Animal():

    def __init__(self):
        print("Animal created")
    def whoAmI(self):
       print("ANIMAL")
    def eat(self):
        {
           print("EATING")
        }    
class Dog(Animal):
    def __init__(self):
        #Animal.__init__(self)
        print("DOG CREATED")
myd = Dog()
myd.whoAmI()
myd.eat()        