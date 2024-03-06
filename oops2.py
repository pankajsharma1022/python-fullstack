#class Dog():
#    def __init__(self,breed):
#        self.breed=breed
#mydog=Dog(breed="lab")
#print(mydog.breed)    
# we can add more attributes also
#class Dog():
#    def __init__(self,breed,name):
#        self.breed=breed
#        self.name=name
#mydog = Dog("Lab","sammy")
#print(mydog.breed)
#print(mydog.name)       

# class object attribute
#class Dog():

# here species is a class object attribute
#   species ="mammal"
#   def __init__(self,breed,name):
#      self.breed=breed
#      self.name=name

#mydog = Dog("lab","sammy")
#print(mydog.breed)
#print(mydog.name)
#print(mydog.species) 


#######################33333
class circle():
    pi = 3.14

    def __init__(self,radius=1):
        self.radius=radius
    def area(self):
        return self.radius*self.radius*circle.pi
    def set_radius(self,new_r):
        self.radius = new_r

myc = circle(3)        
myc.set_radius(999)
print(myc.area())