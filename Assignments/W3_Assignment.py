# Creating the function
def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        final_price = price - (price*discount_percent/100)
        return final_price
    else:
        return price
    
# Prompting user for input 
price = float (input ("Enter the original price of the item: "))
discount_percent = float (input ("Enter the percentage discount: "))

# Calling the function and printing the final output 
print ("The final price is: ",calculate_discount(price,discount_percent))
