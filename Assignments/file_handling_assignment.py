# The try clause
try:
    # File creation and adding text
    with open("my_file.txt", "w") as file:
        file.write("Hello World! \n")
        file.write("My name is Sharon. \n")
        file.write("My contact number is +254 700123456. \n")

    # File reading and display
    print("Contents of my_file.txt: \n")
    with open("my_file.txt", "r") as file:
        contents=file.read()
        print(contents)

    # File appending 
    with open("my_file.txt", "a") as file:
        file.write("I am pursuing a software development course at PLP academy. \n")
        file.write("My passion lies in hardware and software programming. \n")
        file.write("Languages: Python, Dart, HTML, CSS etc.\n")
        print("New lines added successfully.")

# except clauses for potential file related exceptions
except FileNotFoundError:
    print ("Error: The file you are trying to access cannot be found.")
except PermissionError:
    print("Error: You do not have the permission to access this file.")
finally: 
    print("Script execution completed.")
