import threading
from datetime import datetime
from database_config.db_settings import execute_query
from decorator.decorator import log_decorator


@log_decorator
def add_order():
    order_date = input("Enter order date (YYYY-MM-DD HH:MM:SS): ")
    total_amount = input("Enter total amount: ")
    user_id = input("Enter user ID: ")
    restaurant_id = input("Enter restaurant ID: ")
    branch_id = input("Enter branch ID: ")

    query = '''INSERT INTO orders (order_date, total_amount, user_id, restaurant_id, branch_id) 
               VALUES (%s, %s, %s, %s, %s)'''
    params = (order_date, total_amount, user_id, restaurant_id, branch_id)
    threading.Thread(target=execute_query(query, params)).start()
    print("Order added successfully!")


@log_decorator
def add_courier():
    name = input("Enter courier's name: ")
    phone_number = input("Enter courier's phone number: ")
    vehicle_type = input("Enter courier's vehicle type: ")
    current_location = input("Enter courier's current location: ")
    user_id = input("Enter user ID: ")

    query = '''INSERT INTO couriers (name, phone_number, vehicle_type, current_location, user_id) 
               VALUES (%s, %s, %s, %s, %s)'''
    params = (name, phone_number, vehicle_type, current_location, user_id)
    threading.Thread(target=execute_query(query, params)).start()
    print("Courier added successfully!")


@log_decorator
def add_restaurant():
    name = input("Enter restaurant's name: ")
    description = input("Enter restaurant's description: ")
    phone_number = input("Enter restaurant's phone number: ")
    address = input("Enter restaurant's address: ")
    logo = input("Enter restaurant's logo: ")
    user_id = input("Enter user ID: ")

    query = '''INSERT INTO restaurants (name, description, phone_number, address, logo, user_id) 
               VALUES (%s, %s, %s, %s, %s, %s)'''
    params = (name, description, phone_number, address, logo, user_id)
    threading.Thread(target=execute_query(query, params)).start()
    print("Restaurant added successfully!")


@log_decorator
def add_branch():
    name = input("Enter branch's name: ")
    address = input("Enter branch's address: ")
    phone_number = input("Enter branch's phone number: ")
    restaurant_id = input("Enter restaurant ID: ")
    user_id = input("Enter user ID: ")

    query = '''INSERT INTO branches (name, address, phone_number, restaurant_id, user_id) 
               VALUES (%s, %s, %s, %s, %s)'''
    params = (name, address, phone_number, restaurant_id, user_id)
    threading.Thread(target=execute_query(query, params)).start()
    print("Branch added successfully!")


@log_decorator
def add_kitchen_menu():
    name = input("Enter menu item name: ")
    description = input("Enter menu item description: ")
    price = input("Enter menu item price: ")
    restaurant_id = input("Enter restaurant ID: ")

    query = '''INSERT INTO kitchen_menu (name, description, price, restaurant_id) 
               VALUES (%s, %s, %s, %s)'''
    params = (name, description, price, restaurant_id)
    threading.Thread(target=execute_query(query, params)).start()
    print("Kitchen menu item added successfully!")


@log_decorator
def add_order_item():
    order_id = input("Enter order ID: ")
    kitchen_id = input("Enter kitchen item ID: ")
    quantity = input("Enter quantity: ")
    price = input("Enter price: ")

    query = '''INSERT INTO order_item (order_id, kitchen_id, quantity, price) 
               VALUES (%s, %s, %s, %s)'''
    params = (order_id, kitchen_id, quantity, price)
    threading.Thread(target=execute_query(query, params)).start()
    print("Order item added successfully!")


@log_decorator
def add_delivery():
    order_id = input("Enter order ID: ")
    courier_id = input("Enter courier ID: ")
    assigned_time = datetime.now()
    delivery_date = input("Enter delivery date (YYYY-MM-DD HH:MM:SS): ")

    query = '''INSERT INTO delivery (order_id, courier_id, assigned_time, delivery_date) 
               VALUES (%s, %s, %s, %s)'''
    params = (order_id, courier_id, assigned_time, delivery_date)
    threading.Thread(target=execute_query(query, params)).start()
    print("Delivery added successfully!")


@log_decorator
def add_payment():
    order_id = input("Enter order ID: ")
    payment_date = input("Enter payment date (YYYY-MM-DD HH:MM:SS): ")
    amount = input("Enter amount: ")
    payment_method = input("Enter payment method: ")

    query = '''INSERT INTO payments (order_id, payment_date, amount, payment_method) 
               VALUES (%s, %s, %s, %s)'''
    params = (order_id, payment_date, amount, payment_method)
    threading.Thread(target=execute_query(query, params)).start()
    print("Payment added successfully!")
