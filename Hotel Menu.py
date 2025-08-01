
MENU = {
    1: {"item": "Paneer Tikka", "price": 280.00},
    2: {"item": "Vegetable Biryani", "price": 250.00},
    3: {"item": "Dal Makhani", "price": 220.00},
    4: {"item": "Garlic Naan", "price": 60.00},
    5: {"item": "Gulab Jamun", "price": 120.00},
    6: {"item": "Paneer Toofani", "price": 240.00},
}

GST_RATE = 0.18 


def display_menu():
  
    print("----------- Welcome TO AK Restaurant -----------")
    print("                     MENU")
    print("------------------------------------------------------")
    print("No. | Item                | Price")
    print("------------------------------------------------------")
    for key, value in MENU.items():
        
        print(f"{key:<3} | {value['item']:<19} | ₹{value['price']:.2f}")
    print("------------------------------------------------------")
    print("Enter '0' when you have finished ordering.")
    print("------------------------------------------------------")



def take_order():
   
    order = []
    while True:
        try:
            choice = int(input("Enter the item number you wish to order: "))
            if choice == 0:
             
                break
            elif choice in MENU:
                
                ordered_item = MENU[choice]
                order.append(ordered_item)
                print(f"Added '{ordered_item['item']}' to your order.")
            else:
                
                print("Invalid item number. Please choose from the menu.")
        except ValueError:
            
            print("Invalid input. Please enter an item number.")
    return order



def generate_bill(order):
    
    if not order:
        print("No items were ordered.")
        return

    subtotal = 0.0
    print("\n\n----------- FINAL BILL -----------")
    print("----------------------------------")
    print("Item                | Price")
    print("----------------------------------")

    # Calculate subtotal and print each item
    for item in order:
        print(f"{item['item']:<19} | ₹{item['price']:.2f}")
        subtotal += item['price']

    print("----------------------------------")
    # Calculate GST and the final total
    gst_amount = subtotal * GST_RATE
    total_amount = subtotal + gst_amount

    # Print the totals
    print(f"{'Subtotal:':<19} | ₹{subtotal:.2f}")
    print(f"{'GST (18%):':<19} | ₹{gst_amount:.2f}")
    print("----------------------------------")
    print(f"{'GRAND TOTAL:':<19} | ₹{total_amount:.2f}")
    print("----------------------------------")
    print("Hamare restaurant ma aane ke liye dhanyvad,Wapas Aate rahiyega ")
    print("---------------------------------------------------------------")



if __name__ == "__main__":
    display_menu()
    customer_order = take_order()
    generate_bill(customer_order)