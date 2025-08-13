#Question 1
def calculate_discount(price, discount_percentage):
    """
    Calculates the final price after applying a doscount.   
    """
    if discount_percentage >= 0.20:
        final_price = price * (1 - discount_percentage)
    else:
        final_price = price
    return final_price

print(f"Price to pay: Ksh{calculate_discount(400, 0.10)}")

#Question 2
price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage (as a decimal): "))

final_price = calculate_discount(price, discount_percentage)
if discount_percentage >= 0.20:
    print(f"Discount applied, price to pay: Ksh{final_price}")
else:
    print("No discount applied, original price remains: Ksh{price}")
