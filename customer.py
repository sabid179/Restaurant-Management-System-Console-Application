class Customer:

    def __init__(self, name, email, address, initial_balance):
        self.name = name
        self.email = email
        self.address = address
        self.__balance = initial_balance
        self.my_orders = []
        
        
    def view_menu(self, restaurant):
        restaurant.show_menu()
        
        
    def place_order(self, restaurant, item_dict):
        new_order = restaurant.place_order(self, item_dict)
        if new_order is not None:
            self.my_orders.append(new_order)
        
    
    def money_decrease_by(self, amount):
        self.__balance -= amount    
    
    
    @property
    def available_balance(self):
        return self.__balance
    
    
    def has_enough_balance(self, required_amount):
        return self.__balance >= required_amount
    
    
    def view_past_orders(self):
        if len(self.my_orders) == 0:
            print('\nYou dont have ordered before..!')
            return
        
        order_count = 1
        for each_order in self.my_orders:
            print()
            print(f'# Order no. [{order_count}]:')
            each_order.view_order_details()
            order_count += 1
            
        return
    
    
    def add_funds(self, amount):
        if amount < 0:
            print("\nSuspicious Transaction..!")
            return
        
        self.__balance += amount
        print('\nFunds Added Successfully..!')
        
        
    def withdraw_money(self):
        if self.__balance > 0:
            print(f"\n{self.__balance} TK Withdrawal Success..!")
            print(f"Current Balance {self.__balance} TK")
            self.__balance = 0.0
            
        else:
            print("Balance is Empty..! HeHe goribs..")
