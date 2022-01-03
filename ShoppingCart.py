from product import Product

class Shopping_cart:

  
  def __init__(self, product, price, category):
    # self.product = ['item1', ' item2', 'item3']
    self.product_list = []
    self.price = []
    self.category = []


  #Add new items to cart
  def add_to_cart(self):
    self.product_list.append(Product(''))

    #append items in list
    pass



  #calculate and return current total of all products in cart  
  def get_cart_total(self):
    number_items_cart = len(self.price)
    cart_total = sum(self.price)
    #items in cart
    #price of items
    #add items together
    #print/return total
    print(f'You have {number_items_cart} items in your cart. The total comes to {cart_total}')
  

  
  
  def empty_cart():
    
    pass


  def add_to_shopping_cart():
    current_cart = shopping_cart

    pass


  def view_cart(self):
    shopping_cart = self.product_list
    for items in shopping_cart:
      print(item)
    #loop cart's product list
    #print each product to terminal
    pass
