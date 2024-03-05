
print("Hello there!") 

# Variable assignment
Name = name= 'Sharon'
print("My name is", name)

age = 29
print("The datatype of", age, "is", type(age), "while that of",name, "is", type(name))

# This is a list datatype (sequence) --they're mutable
languages = ["English","Swahili","French"]
print("I speak", languages[0])

#This is tuple datatype (sequence) --immutable
product = ("X-box", 500.21, "GTO", 287)
print(product[0],":",product[1])

#This is a set --holds unordered collection of items
student_id = {112,115,67,312,890} 
print (student_id)

#Dict (Dictionary) data type, stores elements in the form of key:value pairs,values can be retrieved using keys e.g
capital_city={"Kenya": "Nairobi", "U.S.A":"Washington DC"}
print(capital_city)
print("The capital city of Kenya is", capital_city["Kenya"])

# implicit conversion - automatic
num_int = 100
num_float = 120.59
num_sum = num_int + num_float

print ("The sum is:",num_sum, "and is of type", type(num_sum))

#explicit conversion - manual type conversion, also called typecasting
num2_sum = num_int + int(num_float)
print("The 2nd sum is", num2_sum,"and is of type",type(num2_sum))

# Basic Operations 
x=8
y=17
print ("sum =",x+y)
print ("Subtraction = ", y-x)
print("Division = ", y/x)
print("Multiplication = ",x*y)
print("Floor division = ", y//x)
print ("Modulo = ", y%x)
print("Is x greater than y? Answer:", x>y) # comparison operators
print ("Is x equal to y? Answer:", x==y)
print("Is x not equal to y? Answer:", x!=y)
print(y>x and x!=y) #logical and operator

student_id = {112,115,67,312,890}
print ("Is 112 present in the sequence? Answer:",112 in student_id) #membership operator to check if 112 is in the sequence

student_name = input("Please enter your name:")
print("The name you entered is:" + student_name)

"""
x={}
x[2]=10
x[1]=[20,30,40]
print(x[1][2])

name = "Testing"
print(len(name))
"""