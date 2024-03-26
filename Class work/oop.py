'''
# First example, Understanding OOP -- Classes,attributes,methods,objects
# initiate class 
class Person:
    school = ""  #class attribute
    def __init__(self,name,age,school): #constructor
        self.name = name #instance attributes 
        self.age = age
        self.school = school
 
    #class method
    def displayInfo(self):
        print ("Name:",self.name)
        print ("Age:", self.age)
        print ("School:",self.school)

#creating an object (instance of a class)
#assigning values 
details = Person("Rommie",24, "PLP Academy")

#call the method
details.displayInfo()



# Abstraction example
class Vehicle: #base class
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        raise NotImplementedError("Subclass must implement this abstract method")

    def stop(self):
        raise NotImplementedError("Subclass must implement this abstract method")
    
class Car(Vehicle): #subclass inherited from vehicle
    def start(self):
        return f"The {self.year} {self.make} {self.model} starts"
    
        #The 'f' indicates an f-string, allowing inclusion of variables inside curly braces {}

    def stop(self):
        return f"The {self.year} {self.make} {self.model} stops"


# Creating instances of Car
my_car = Car("Toyota", "Camry", 2020)

# Using the start and stop methods without needing to know the internal implementation
print(my_car.start())
print(my_car.stop())
'''

