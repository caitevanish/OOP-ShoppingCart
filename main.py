from customer import Customer
from product import Product
from ShoppingCart import Shopping_cart

customer_1 = Customer("Charlie")

# - DONE - [CUSTOMER] print customer's name to the terminal 
print(customer_1.customer_name)

# -- [SHOPPING CART] Call the customer’s add product to shopping cart method three times and add the three products objects you create
customer_1.add_to_cart("Gummy Bears", 2, "gummies")
customer_1.add_to_cart("Bon-Bons", 5, "chocolate")
customer_1.add_to_cart("Taffy", 4, "misc")


# -- [CUSTOMER] Call the customer’s view products method
customer_1.view_cart()


# -- [] Call the customer’s shopping cart’s get cart total method.
customer_1.get_cart_total

# -- [] Capture the total the method returns in a variable and print to the terminal

# -- [] Call the customer’s shopping cart’s empty cart method

# -- [] Check if all products have been removed from the shopping cart

#