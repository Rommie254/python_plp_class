# Creating class Person
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    # Method that prints introductory message
    def introduce (self):
        print (f"My name is {self.name}, I am {self.age} years old, and I am {self.gender}.")

# Creating instance of the class
person = Person("Lauren", 29, "non-binary")

# Calling the method
person.introduce()

        