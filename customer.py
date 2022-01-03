from ShoppingCart import Shopping_cart

class Customer:
  def __init__(self, customer_name):
      self.customer_name = ''
      # self.shopping_cart = shopping_cart


  def add_customer(self):
    self.customer_name = input('Whats your name?: ')
    print(f"Hello, {self.customer_name}")


