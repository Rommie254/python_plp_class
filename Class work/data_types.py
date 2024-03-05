'''
# STRINGS IN PYTHON
plp_str="Welcome to PLP Academy "
print(plp_str)
print(plp_str[0]) #slicing--prints first char
print(plp_str[-1])#prints last char
print(plp_str[11:14]) #prints PLP

student_str='Python Class'
print(plp_str + student_str)
print(plp_str * 2) # *is the repetition operator


# LISTS IN PYTHON --separated by commas, enclosed in square brackets[], can store different data types, lists are mutable
academy_ls = ["Jack", 30, 3, 4.2, 2+8j, 'Thika']
student_ls=[30,2+8j]
print (academy_ls)
print (academy_ls[0])
print (academy_ls[3:6]) # for sliced lists, the start index is inclusive but the end index is exclusive
print (academy_ls + student_ls) # can also use extend () function
print (student_ls*3)
student_ls.append(49)
print (student_ls)
student_ls[0]=2
print (student_ls)
del student_ls[2] #can alos use remove()
print (student_ls)

#Iterating through a LIST using FOR loop
languages=["Python", "Dart", "HTML", "CSS"]
for language in languages:
    print(language)


#TUPLES IN PYTHON --separated by commas, enclosed within parenthesis()-optional, can store different data types, tuples are immutable ie read-only
my_tuple = ('abcd',786, 2.3, 'John', 70.2)
tiny_tuple = 123, 6+2j, 'John'
print(my_tuple)
print(my_tuple[2:3])
print(my_tuple+tiny_tuple)
print(tiny_tuple*4)


#DICTIONARY DATATYPE-- consists of key:value pairs, separated by comma, enclosed in curly brackets
my_dict = {} #empty dictionary
tinydict={'name':'john', 'code':6734, 'dept':['sales']}
print(tinydict)
print(tinydict.keys()) #prints keys only
print(tinydict.values())#prints values


capital_city = {"Kenya":"Nairobi", "Rwanda":"Kigali"}
print ("Initial Dictionary:", capital_city)
capital_city["Sudan"]="Khartoum"
print ("Updated Dictionary: ",capital_city)

#Dictionar membership test for keys
print ("Kenya" in capital_city)

#Iterating through a dictionary
for city in capital_city:
    print(city)

#SET stores unique data, cannot be duplicated, inside curly braces {} separated by commas (unordered hence no indexing)
studentID = {201,461,782, 901,201}
print ("Student ID's:", studentID)
studentID.add(873)
print ("New Student ID's:", studentID)
studentID.discard(782)
print ("After applying remove():", studentID)


#Union of 2 sets:includes all alements of set 1 & 2
A = {1,3,5}
B = {0,2,4}
print ("Union using |:", A|B)
print ("Union using union():", A.union(B))

#Set intersection - includes common elements between the 2 sets 
A = {1,3,5}
B = {1,2,3}
print ("Intersection using &:", A&B)
print ("Intersection using intersection():", A.intersection(B))

#Set Difference:elements in 1 not present in 2
print ("Difference using -:", A-B)
print ("Difference using difference():", A.difference(B))
print ("Symmetric Difference using ^:", A^B)
print ("Difference using method:", A.symmetric_difference(B))

# Using f-strings
name = "Sha"
country = "Kenya"
print (f'{name} comes from {country}.')
'''

'a' + 'x' if '123'.isdigit() else 'y' + 'b'