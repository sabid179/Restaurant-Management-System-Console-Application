from datetime import datetime


class Order:
    
    def __init__(self, customer, restaurant):
        self.customer = customer
        self.restaurant = restaurant
        self.order_date = datetime.now().strftime('%d-%m-%Y')
        self.order_items = {}
        self.total_cost = 0.0
        self.discount_percentage = self.restaurant.running_discount_percentage
        
    
    def add_item_to_order(self, food_item, item_quantity):
        self.order_items[food_item] = item_quantity
        self.total_cost += food_item.item_price * item_quantity
        
    
    @property
    def get_bill(self):
        return self.total_cost - (self.total_cost * (self.discount_percentage / 100))
    
    
    def view_order_details(self):
        print(f"Restaurant Name : {self.restaurant.restaurant_name}")
        print(f"Ordered by      : {self.customer.name}")
        print(f"Order Date      : {self.order_date}")
        print(f"Order items     :")
        
        item_count = 1
        for each_item in self.order_items:
            print(f'-> Item [{item_count}]:')
            each_item.print_item()
            if item_count != len(self.order_items):
                print()
            item_count += 1
        
        print(f'Total Cost      : {self.total_cost} TK')
        print(f'Discount Applied: {self.discount_percentage} %')
        print(f'Final Amount    : {self.get_bill} TK')
