import random
orders = []
def order_id():
    r1 = random.randint(0,9)
    r2 = random.randint(0,9)
    r3 = random.randint(0,9)
    r4 = random.randint(0,9)
    r5 = random.randint(0,9)
# Function to take orders
def take_order(orders):
    print("Menu:")
    print("1. Burger - 120")
    print("2. Pizza - 250")
    print("3. Pasta - 70")
    print("4. Noodles - 100")
    
    order = input("Enter the item number you want to order (1/2/3/4): ")
    
    if order == '1':
        orders.append("Burger")
    elif order == '2':
        orders.append("Pizza")
    elif order == '3':
        orders.append("Pasta")
    elif order == '4':
        orders.append("Noodles")
    else:
        print("Invalid choice. Please select a valid item.")
        take_order()

# Function to display orders
def display_orders(orders):
    if not orders:
        print("No orders yet.")
    else:
        print("Current Orders:")
        print(orders)
        
# Main loop
while True:
    print("\nRestaurant Management System")
    print("1. Take Order")
    print("2. Display Orders")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if int(choice) == 1:
       take_order(orders)
    elif int(choice) == 2:
        display_orders(orders)
    elif int(choice) == 3:
        print("Thank you for choosing us")
        break
    else:
        print("Invalid choice. Please select a valid option.")
