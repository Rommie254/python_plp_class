#Functions --block of reusable code that performs a specific task, defined using 'def' keyword 
'''
def add_num():
    print (10+30)

add_num()

def add_num2(a,b):
    addition = a+b
    return addition

print("The sum is:", add_num2(2,5))

#Function to determine a palindrome from user input
def isPalindrome(word):
    if (word == word[::-1]):
        print (word,"is a Palindrome")
    else:
        print(word, "is not a Palindrome")

word = input ("Enter a string/word: ")
isPalindrome(word)

# Lambda Function --anonymous, nameless function (used for simple expressions)
snack = lambda: print ("Fav Snack: Yoghurt")
snack()

sum = lambda x,y: x+y
print ("The sum is:", sum(3,8))

#Classes
class Python_Switch:
    def day(self,month):

        default="Incorrect day"

        return getattr(self,'case_'+str(month),lambda:default)()
    
    def case_1(self):
        return "Jan"
    def case_2(self):
        return "Feb"
    def case_3(self):
        return "Mar"
switch = Python_Switch()

print(switch.day(1))
print(switch.day(2))
print(switch.day(3))
'''
list1 = [3 , 2 , 5 , 6 , 0 , 7, 9]
sum = 0
sum1 = 0
for elem in list1:
    if (elem % 2 == 0):
        sum = sum + elem
        continue
    if (elem % 3 == 0):
        sum1 = sum1 + elem
print(sum , end=" ")