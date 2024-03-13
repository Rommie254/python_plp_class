'''
#FOR loop
words = ["one", "two", "three"]
for x in words:
    print(x)

# FOR loop: Using Range --performs action repeatedly as specified in range
name = "Rommie"

for i in range(4):
    print(name)


#WHILE loop --perfom incrementation
i=1
while i<=6:
    print(i)
    i+=1


#Loop Controls: Break & Continue 
#break --terminates loop when encountered 
x=12
while x>10:
    print ("x:", x)
    if x==20:
        print("Breaking...")
        break
    x +=1

print("End")


colors = ["white","red","maroon","cyan","black","blue"]
for color in colors:
    print(color)
    if color == "cyan":
        print("I've got the color I want")
        break
    

colors = ["white","red","maroon","cyan","black","blue"]
count = 0
length = len(colors)

while count < length:
    print (colors[count])
    if colors[count] == "cyan":
        print("I've got the color I want")
        break
    count +=1


# Continue --used to skip the current iteration and go to the next
ages = [29, 36, 50, 20, 43, 19, 34]
for age in ages:
    if age < 21:
        continue
    print (age)
'''
# List comprehensions 
nums = [2, 6, 21, 7, 52]
doubled = [num*2 for num in nums]
print (doubled)

