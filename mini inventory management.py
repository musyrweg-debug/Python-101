#--------INVENTORY MANAGEMENT SYSTEM--------#
inventory = []
def add_item():
    while True:
        item_name = input("enter item name:")
        item_quantity = int(input("enter item quantity:"))  
        item_price = float(input("enter item price:"))
        break
    item_data = {
            "name": item_name,
            "quantity": item_quantity,
            "price": item_price
        }
    inventory.append(item_data)
    print("Inventory updated successfully!")

    
def view_inventory():
    print("Inventory Content:")
    for item_data in inventory:
        print(f"""
              Name of item: {item_data['name']}
              Quantity: {item_data['quantity']}
              Price: {item_data['price']}
              """)
        
def search_item():
    search = input("Enter item name to search:")
    print({search})
    for item_data in inventory:
        if item_data["name"]== search:
            print(f"""
                  Name of the item: {item_data["name"]}
                  Quantity: {item_data["quantity"]}
                  Price: {item_data["price"]}
                  """)
            break
        else:
            print("Item not found in inventory.")

def low_stock():
    for item_data in inventory:
        if item_data["quantity"] < 10:
            print(f"Item {item_data["name"]} is low in stock with quantity {item_data["quantity"]}")
            break
        else:
            print(f"Item {item_data["name"]} is sufficiently stocked with quantity {item_data["quantity"]}")

def stock_value():
    total_value = 0
    for item_data in inventory:
        item_value = item_data["quantity"] * item_data["price"]
        total_value =+ item_value
    print(f"Total stock value: {total_value}")

def stock_balance():
    sales = int(input("Enter quantity of items sold:"))
    for item_data in inventory:
        if item_data["quantity"] >= sales:
            item_data["quantity"] -= sales
            print(f"New stock balance is {item_data["quantity"]}")
            break
        else:
            print("Insufficient stock to complete the sale.")

def remove_product():
    old_product = input("Enter product name to be removed:")
    for item_data in inventory:
        if item_data["name"] == old_product:
            inventory.remove(item_data)
            print(f"Item {old_product} removed successfully!")
            break
    else:
        print("Item is not present in inventory!")

product_info = []
def product_categories():
    category = input("Enter product category:")
    name = input("Enter product name:")
    price = float(input("Enter product price:"))
    quantity = int(input("Enter product quantity:"))
    product_data = {
        category: {"name": name, "price": price, "quantity": quantity}
    }
    product_info.append(product_data)
    print("Product category added successfully!")

def system_menu():
    print("""
          CHOOSE AN OPTION:
    1. Add item
    2. View inventory
    3. Search item
    4. Low stock alert
    5. Stock value calculation
    6. Stock balance update
    7. Remove product
    8. Product categories
    """)
    choice = input("Enter your choice:")
    while True:
        if choice == "1":
            add_item()
        elif choice == "2":
            view_inventory()    
        elif choice == "3":
            search_item()
        elif choice == "4":
            low_stock()
        elif choice == "5":
            stock_value()
        elif choice == "6":
            stock_balance()
        elif choice == "7":
            remove_product()
        elif choice == "8":
            product_categories()
            break
        else:
            print("Invalid choice, try again")
            
if __name__ == "__main__":
    system_menu()
         
