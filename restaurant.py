from menu import Menu
from food_item import FoodItem
from order import Order

class Restaurant:
    
    def __init__(self, restaurant_name, first_investment):
        self.restaurant_name = restaurant_name
        self.menu = Menu('primary_menu')
        self.customers = []
        self.order_history = []
        self.__balance = first_investment
        self.running_discount_percentage = 0.0
        
        
    def recruit_admin(self, admin):
        self.admin = admin
    
    
    def get_menu(self):
        return self.menu
    
    
    def add_item_to_menu(self, item_name, item_price):
        food_item = FoodItem(item_name, item_price)
        self.menu.add_food_item(food_item)
        
        
    def remove_item_from_menu(self, item_name):
        food_item = None
        food_menu = self.menu.food_items
        
        for each_item in food_menu:
            if each_item.item_name.lower() == item_name.lower():
                food_item = each_item
                break
        
        if food_item is None:
            print('\nNo item matches this argument..!')
        else:
            self.menu.remove_food_item(food_item) 
    
    
    def add_customer(self, customer):
        self.customers.append(customer)
        
        
    def check_customer_details(self, customer):
        if customer is not None:
            print(f'   Name    : {customer.name}')
            print(f'   Email   : {customer.email}')
            print(f'   Address : {customer.address}')
        else:
            print('\nNo Customer found by this name..!')
            return
        
        
    def get_all_customers(self):
        return self.customers
    
    
    def place_order(self, customer, item_dict):
        new_order = Order(customer, self)
        at_least_one_item_ordered = False
        
        print()
        for item_name in item_dict:
            food_item = self.menu.get_item(item_name)
            if food_item is not None:
                should_pay = food_item.item_price * item_dict[item_name]
                if customer.has_enough_balance(should_pay):
                    new_order.add_item_to_order(food_item, item_dict[item_name])
                    print(f'{item_name} ordered successfully..!')
                    at_least_one_item_ordered = True
                    customer.money_decrease_by(should_pay)
                else:
                    print(f'{item_dict[item_name]} ta {item_name} tere aukad se bahar hai..')
                    print('Add Some Funds...')
            else:
                print(f'{item_name} is not available..!')
        
        if at_least_one_item_ordered:
            print('Your order has been placed..!')
            self.order_history.append(new_order)
            return new_order
        else:
            return None
    
    def admin_login(self, username):
        if username.lower() == self.admin.name:
            return self.admin
        else:
            return None
    
    
    def customer_login(self, username):
        for customer in self.customers:
            if username.lower() == customer.name.lower():
                return customer
        return None
        
        
    def show_menu(self):
        self.menu.view_menu()
        
        
    def update_discount_percentage(self, new_discount_percentage):
        self.running_discount_percentage = new_discount_percentage
