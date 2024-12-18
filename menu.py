class Menu:
    
    def __init__(self, menu_title):
        self.menu_title = menu_title
        self.food_items = []
        
        
    def add_food_item(self, food_item):
        self.food_items.append(food_item)
        print('\nFood item added successfully..!')
        
        
    def remove_food_item(self, food_item):
        try:
            self.food_items.remove(food_item)
            print('\nItem removed successfully..!')
        except Exception:
            print('\nNo item matches this argument..!')
            
            
    def get_item(self, item_name):
        for food_item in self.food_items:
            if food_item.item_name.lower() == item_name.lower():
                return food_item
        return None

            
    def view_menu(self):
        print('\n[__FOOD MENU__]\n')
        
        if len(self.food_items) == 0:
            print('Menu is Empty!')
            return
        
        item_count = 1
        for each_item in self.food_items:
            print(f'-> Item [{item_count}]:')
            each_item.print_item()
            if item_count != len(self.food_items):
                print()
            item_count += 1
        
        return
