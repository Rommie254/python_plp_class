# FILE HANDLING IN PYTHON

# open file for writng and add some text
file1=open("Example.txt", "w")

file1.write("Hello World! \n")
file1.write("This is my first Python file.")
file1.close()

# open file for reading and read (print) the contents 
with open("Example.txt","r") as file2:
    content=file2.read()
    print(content)
    print(file2.name)
    print(file2.closed)
    print(file2.mode)
    
print(file2.closed)    

# deleting a file 
import os
filename = "Example.txt"
if os.path.exists(filename):
    os.remove(filename)
    print(f"{filename} has been deleted.")
else:
    print(f"{filename} does not exist.")



