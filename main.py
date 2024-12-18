from restaurant import Restaurant
from admin import Admin


def initial_interface():
    print("""\n[__LOGIN OPTIONS__]\n
    A | Admin Login
    B | Customer Login
    C | Exit
    """.upper())


def admin_options():
    print("""\n[__ADMIN OPTIONS__]\n
    A | Create Customer Account
    B | Remove Customer Account
    C | View All Customers
    D | Manage Restaurant Menu
    E | Exit
    """.upper())
    
    
def customer_options():
    print("""\n[__CUSTOMER OPTIONS__]\n
    A | View Restaurant Menu
    B | Check Available Balance
    C | Add Balance to Wallet
    D | Withdraw Remaining Money
    E | Place an Order
    F | View Past Orders
    G | Exit
    """.upper())


def get_command():
    command = input(">>> Select an option: ")
    return command.upper()


def collect_customer_data():
    customer_name = input(">>> Enter Customer Name    : ")
    customer_email = input(">>> Enter Customer Email   : ")
    customer_address = input(">>> Enter Customer Address : ")

    return customer_name, customer_email, customer_address


def manage_menu_options():
    print("""\n[__MANAGE MENU OPTIONS__]\n
    A | Create a New Empty Menu
    B | Add a New Item
    C | Remove an Item
    D | Update Price
    E | View Menu
    F | Exit
    """.upper())
    
    
def get_items_input():
    order_items = {}
    
    while (True):
        item_name = input(">>> Enter Item Name      : ")
        quantity = int(input (">>> Enter Quantity       : "))
        order_items[item_name] = quantity
        user_command = input(">>> Add More Items? (y/n): ")
        if user_command.lower() != 'y':
            break
    
    return order_items
            
    
def collect_food_item_info():
    item_name = input(">>> Enter Item Name    : ")
    item_price = input(">>> Enter Item Price   : ")
    
    return item_name, float(item_price)


def main():
    # Creating Hotel Object and Recruiting Admin
    baper_hotel = Restaurant('Baper Hotel', 0.0)
    baper_hotel.recruit_admin(Admin('admin', baper_hotel))
    
    while True:
        initial_interface()
        user_command = get_command()
        
        if user_command == 'A':
            # Admin Login
            username = input(">>> Enter Username ['admin']: ")
            restaurant_admin = baper_hotel.admin_login(username)
            if restaurant_admin is not None:
                print("\nLogin Successful..!")
            else:
                print("\nWrong Credential..\nTry again...")
                continue
            
            # Admin Options
            while True:
                admin_options()
                admin_command = get_command()
                
                if admin_command == 'A':
                    # Create Customer Account
                    customer_name, customer_email, customer_address = collect_customer_data()
                    
                    restaurant_admin.add_new_customer(customer_name, customer_email, customer_address)
                    
                elif admin_command == 'B':
                    # Remove Customer Account
                    customer_name = input(">>> Enter Customer Name    : ")
                    restaurant_admin.remove_a_customer(customer_name)
                
                elif admin_command == 'C':
                    # View All Customers
                    restaurant_admin.view_all_customers()
                    
                elif admin_command == 'D':
                    # Manage Restaurant Menu
                    while True:
                        manage_menu_options()
                        admin_command = get_command()
                        
                        if admin_command == 'A':
                            # Create a New Menu
                            restaurant_admin.create_a_new_menu()
                            
                        elif admin_command == 'B':
                            # Add a New Item
                            item_name, item_price = collect_food_item_info()
                            restaurant_admin.add_item_to_menu(item_name, item_price)
                            
                        elif admin_command == 'C':
                            # Remove an Item
                            item_name = input(">>> Enter Item Name    : ")
                            restaurant_admin.remove_item_from_menu(item_name)

                        elif admin_command == 'D':
                            # Update Price
                            item_name, new_price = collect_food_item_info()
                            restaurant_admin.update_price_for_an_item(item_name, new_price)
                            
                        elif admin_command == 'E':
                            # View Menu
                            restaurant_admin.view_menu()
                        
                        else:
                            # Exit
                            print(">>> Exiting...")
                            break
                    
                else:
                    # Exit
                    print(">>> Exiting...")
                    break
                
        elif user_command == 'B':
            # Customer Login
            username = input(">>> Enter Customer Name: ")
            customer = baper_hotel.customer_login(username)
            
            if customer is not None:
                print("\nLogin Successful..!")
            else:
                print("\nNo user found by this name..!\nAsk Admin to create an account for you..")
                continue
                
            # Customer Options
            while True:
                customer_options()
                customer_command = get_command()
                
                if customer_command == 'A':
                    # View Restaurant Menu
                    customer.view_menu(baper_hotel)
                
                elif customer_command == 'B':
                    # Check Available Balance
                    print(f"\nAvailable Balance: {customer.available_balance} TK")
                    
                elif customer_command == 'C':
                    # Add Balance to Wallet
                    amount = float(input(">>> Enter Amount: "))
                    customer.add_funds(amount)
                    
                elif customer_command == 'D':
                    # Withdraw Money
                    customer.withdraw_money()
                
                elif customer_command == 'E':
                    # Place an Order
                    order_items = get_items_input()
                    customer.place_order(baper_hotel, order_items)
                    
                elif customer_command == 'F':
                    # View Past Orders
                    customer.view_past_orders()
                
                else:
                    # Exit
                    print(">>> Exiting...")
                    break
            
        else:
            # Exit
            print(">>> Exiting...")
            return
        
        
if __name__ == '__main__':
    main()
