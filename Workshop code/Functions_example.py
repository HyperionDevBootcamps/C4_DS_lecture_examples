'''
Create a program that mimics a simple online store. The program should contain the following functions:

A function to calculate the total cost based on the customer's selected number of goods
A function to apply a 10% discount if the customer spends over 100 
A function to determine if shipping is free: shipping is free if you spend 200, if not you are charged 50 for shipping
A function to calculate the final total cost the customer pays by taking in arguments which will call the other three functions

'''

def calculate_total_cost(quantity, price_per_item):
    return quantity * price_per_item

def apply_discount(total_cost):
    if total_cost > 100:
        return total_cost * 0.9
    else:
        return total_cost

def apply_shipping(total_cost):
    if total_cost >= 200:
        return 0
    else:
        return 50

def calculate_final_total(quantity, price_per_item):
    total_cost = calculate_total_cost(quantity, price_per_item)
    discounted_cost = apply_discount(total_cost)
    shipping_cost = apply_shipping(discounted_cost)
    final_total = discounted_cost + shipping_cost
    return final_total

# Example 

quantity = int(input("Enter how many items you would like to purchase: "))
price_per_item = 30

final_total = calculate_final_total(quantity, price_per_item)
print(f"The final total cost is: {final_total}")
