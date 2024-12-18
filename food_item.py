class FoodItem:
    
    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price
        
        
    def update_price(self, new_price):
        self.item_price = new_price
        
        
    def print_item(self):
        print(f'   Item \t: {self.item_name}')
        print(f'   Price\t: {self.item_price} TK')
