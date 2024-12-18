from customer import Customer
from menu import Menu

class Admin:
    
    def __init__(self, name, restaurant):
        self.name = name
        self.restaurant = restaurant
        
        
    def create_a_new_menu(self):
        new_menu = Menu('menu_by_admin')
        self.restaurant.menu = new_menu
        print('\nNew Menu Created..!')
        
        
    def add_item_to_menu(self, item_name, item_price):
        self.restaurant.add_item_to_menu(item_name, item_price)
        
        
    def update_price_for_an_item(self, item_name, new_price):
        food_item = None
        food_menu = self.restaurant.get_menu()
        food_items = food_menu.food_items
        
        for each_item in food_items:
            if each_item.item_name.lower() == item_name.lower():
                food_item = each_item
                break
        
        if food_item is None:
            print('\nNo item matches this argument..!')
        else:
            food_item.update_price(new_price)
            print(f'\nPrice for {food_item.item_name} has been updated..!')
        
        
    def remove_item_from_menu(self, item_name):
            self.restaurant.remove_item_from_menu(item_name)        
        
    
    def add_new_customer(self, name, email, address):
        new_customer = Customer(name, email, address, 0.0)
        print('\nCustomer account created..!')
        self.restaurant.add_customer(new_customer)
        print('New customer added successfully..!')
        
        
    def view_all_customers(self):
        all_customer_list = self.restaurant.get_all_customers()
        
        if len(all_customer_list) == 0:
            print('\n0 registered customer..!')
            return
        
        print()
        customer_count = 1
        for each_customer in all_customer_list:
            print(f'-> Customer [{customer_count}]:')
            self.restaurant.check_customer_details(each_customer)
            if customer_count != len(all_customer_list):
                print()
            customer_count += 1
        
        return
    
    
    def remove_a_customer(self, customer_name):
        customer = None
        all_customer_list = self.restaurant.get_all_customers()
        
        for each_customer in all_customer_list:
            if each_customer.name.lower() == customer_name.lower():
                customer = each_customer
                break
        
        if customer is None:
            print('\nNo Customer matches this argument..!')
        else:
            self.restaurant.customers.remove(customer)
            print('\nCustomer removed successfully..!')
        
        
    def view_menu(self):
        self.restaurant.show_menu()
