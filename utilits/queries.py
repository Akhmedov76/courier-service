import hashlib
import threading
from datetime import datetime
from database_config.db_settings import execute_query
from decorator.decorator import log_decorator
from email_sender.email_checker import check_email


class Database:

    @log_decorator
    def add_admin(self):
        name = input("Enter name: ").capitalize().strip()
        email = input("Enter email: ").strip()
        phone_number = input("Enter phone number: ").strip()
        address = input("Enter address: ").strip()
        password = hashlib.sha256(input("Password: ").strip().encode('utf-8')).hexdigest()
        role = input("Enter role (user, manager, admin): ").lower().strip()
        try:
            check_email(email)
            query = '''
                    SELECT * FROM users WHERE phone_number=%s OR email=%s
                    '''
            params = (phone_number, email)
            if execute_query(query, params, fetch='one') is not None:
                print("Phone number or email already exists.")
                return False
            query = '''
                    INSERT INTO users (name, email, phone_number, password, address, role)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    '''
            params = (name, email, phone_number, password, address, role)
            execute_query(query, params=params)
            print("Registration successfully")
            return True
        except ValueError:
            print("Invalid input. Please try again.")
            return False
        except Exception as e:
            print(f"An error occurred while adding admin: {str(e)}")
            return False

    def update_admin_table(self):
        admin_id = input("Enter the admin ID: ").strip()
        new_name = input("Enter new name: ").capitalize().strip()
        new_email = input("Enter new email: ").strip()
        new_phone_number = input("Enter new phone number: ").strip()
        new_address = input("Enter new address: ").strip()
        new_role = input("Enter new role (user, manager, admin): ").lower().strip()

        query = '''UPDATE users SET name = %s, email = %s, phone_number = %s, address = %s, role = %s WHERE id = %s'''
        params = (new_name, new_email, new_phone_number, new_address, new_role, admin_id)
        threading.Thread(target=execute_query(query, params)).start()
        print("Admin updated successfully!")
        return None

    @log_decorator
    def delete_admin_table(self):
        admin_id = input("Enter the admin ID: ").strip()

        query = "DELETE FROM users WHERE id = %s"
        params = (admin_id,)
        threading.Thread(target=execute_query(query, params)).start()
        print("Admin deleted successfully!")
        return None

    @log_decorator
    def add_order(self):
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

    def update_order_table(self):
        order_id = input("Enter the order ID: ").strip()
        new_total_amount = input("Enter new total amount: ")

        query = '''UPDATE orders SET total_amount = %s WHERE order_id = %s'''
        params = (new_total_amount, order_id)
        threading.Thread(target=execute_query(query, params)).start()
        print("Order updated successfully!")

    @log_decorator
    def delete_order_table(self):
        order_id = input("Enter the order ID: ").strip()

        query = "DELETE FROM orders WHERE order_id = %s"
        params = (order_id,)
        threading.Thread(target=execute_query(query, params)).start()
        print("Order deleted successfully!")

    @log_decorator
    def get_orders_by_restaurant(self):
        restaurant_id = input("Enter restaurant ID: ").strip()

        query = "SELECT * FROM orders WHERE restaurant_id = %s"
        params = (restaurant_id,)
        threading.Thread(target=execute_query(query, params, fetch='all')).start()
        print("Orders retrieved successfully!")

    @log_decorator
    def add_courier(self):
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
    def update_courier_table(self):
        courier_id = input("Enter the courier ID: ").strip()
        new_name = input("Enter new courier's name: ")
        new_phone_number = input("Enter new courier's phone number: ")
        new_vehicle_type = input("Enter new courier's vehicle type: ")
        new_current_location = input("Enter new courier's current location: ")

        query = '''UPDATE couriers SET name = %s, phone_number = %s, vehicle_type = %s, current_location = %s 
                   WHERE courier_id = %s'''
        params = (new_name, new_phone_number, new_vehicle_type, new_current_location, courier_id)
        threading.Thread(target=execute_query(query, params)).start()
        print("Courier updated successfully!")

    @log_decorator
    def delete_courier_table(self):
        courier_id = input("Enter the courier ID: ").strip()

        query = "DELETE FROM couriers WHERE courier_id = %s"
        params = (courier_id,)
        threading.Thread(target=execute_query(query, params)).start()
        print("Courier deleted successfully!")

    @log_decorator
    def get_couriers_by_restaurant(self):
        id = input("Enter restaurant ID: ").strip()
        query = "SELECT * FROM couriers WHERE restaurant_id = %s"
        params = (id,)
        threading.Thread(target=execute_query(query, params, fetch='all')).start()
        print("Couriers retrieved successfully!")

    @log_decorator
    def add_restaurant(self):
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
    def update_restaurant_table(self):
        restaurant_id = input("Enter the restaurant ID: ").strip()
        new_name = input("Enter new restaurant's name: ")
        new_description = input("Enter new restaurant's description: ")
        new_phone_number = input("Enter new restaurant's phone number: ")
        new_address = input("Enter new restaurant's address: ")
        new_logo = input("Enter new restaurant's logo: ")

        query = '''UPDATE restaurants SET name = %s, description = %s, phone_number = %s, address = %s, logo = %s 
                   WHERE restaurant_id = %s'''
        params = (new_name, new_description, new_phone_number, new_address, new_logo, restaurant_id)
        threading.Thread(target=execute_query(query, params)).start()
        print("Restaurant updated successfully!")

    @log_decorator
    def delete_restaurant_table(self):
        restaurant_id = input("Enter the restaurant ID: ").strip()

        query = "DELETE FROM restaurants WHERE restaurant_id = %s"
        params = (restaurant_id,)
        threading.Thread(target=execute_query(query, params)).start()
        print("Restaurant deleted successfully!")

    @log_decorator
    def add_branch(self):
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
    def update_branch_table(self):
        branch_id = input("Enter the branch ID: ").strip()
        new_name = input("Enter new branch's name: ")
        new_address = input("Enter new branch's address: ")
        new_phone_number = input("Enter new branch's phone number: ")

        query = '''UPDATE branches SET name = %s, address = %s, phone_number = %s 
                   WHERE branch_id = %s'''
        params = (new_name, new_address, new_phone_number, branch_id)
        threading.Thread(target=execute_query(query, params)).start()
        print("Branch updated successfully!")

    @log_decorator
    def delete_branch_table(self):
        branch_id = input("Enter the branch ID: ").strip()

        query = "DELETE FROM branches WHERE branch_id = %s"
        params = (branch_id,)
        threading.Thread(target=execute_query(query, params)).start()
        print("Branch deleted successfully!")

    @log_decorator
    def add_kitchen_menu(self):
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
    def update_kitchen_menu_item(self):
        item_id = input("Enter the menu item ID: ").strip()
        new_name = input("Enter new menu item's name: ")
        new_description = input("Enter new menu item's description: ")
        new_price = input("Enter new menu item's price: ")

        query = '''UPDATE kitchen_menu SET name = %s, description = %s, price = %s 
                   WHERE item_id = %s'''
        params = (new_name, new_description, new_price, item_id)
        threading.Thread(target=execute_query(query, params)).start()
        print("Kitchen menu item updated successfully!")

    @log_decorator
    def delete_kitchen_menu_item(self):
        item_id = input("Enter the menu item ID: ").strip()

        query = "DELETE FROM kitchen_menu WHERE item_id = %s"
        params = (item_id,)
        threading.Thread(target=execute_query(query, params)).start()
        print("Kitchen menu item deleted successfully!")

    @log_decorator
    def add_order_item(self):
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
    def update_order_item(self):
        item_id = input("Enter the order item ID: ").strip()
        new_quantity = input("Enter new quantity: ")
        new_price = input("Enter new price: ")

        query = '''UPDATE order_item SET quantity = %s, price = %s 
                   WHERE item_id = %s'''
        params = (new_quantity, new_price, item_id)
        threading.Thread(target=execute_query(query, params)).start()
        print("Order item updated successfully!")

    @log_decorator
    def delete_order_item(self):
        item_id = input("Enter the order item ID: ").strip()

        query = "DELETE FROM order_item WHERE item_id = %s"
        params = (item_id,)
        threading.Thread(target=execute_query(query, params)).start()
        print("Order item deleted successfully!")

    @log_decorator
    def add_delivery(self):
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
    def update_delivery(self):
        delivery_id = input("Enter the delivery ID: ").strip()
        new_courier_id = input("Enter new courier ID: ")

        query = '''UPDATE delivery SET courier_id = %s 
                   WHERE delivery_id = %s'''
        params = (new_courier_id, delivery_id)
        threading.Thread(target=execute_query(query, params)).start()
        print("Delivery updated successfully!")

    @log_decorator
    def delete_delivery(self):
        delivery_id = input("Enter the delivery ID: ").strip()

        query = "DELETE FROM delivery WHERE delivery_id = %s"
        params = (delivery_id,)
        threading.Thread(target=execute_query(query, params)).start()
        print("Delivery deleted successfully!")

    @log_decorator
    def add_payment(self):
        order_id = input("Enter order ID: ")
        payment_date = input("Enter payment date (YYYY-MM-DD HH:MM:SS): ")
        amount = input("Enter amount: ")
        payment_method = input("Enter payment method: ")

        query = '''INSERT INTO payments (order_id, payment_date, amount, payment_method) 
                   VALUES (%s, %s, %s, %s)'''
        params = (order_id, payment_date, amount, payment_method)
        threading.Thread(target=execute_query(query, params)).start()
        print("Payment added successfully!")

    @log_decorator
    def update_payment(self):
        payment_id = input("Enter the payment ID: ").strip()
        new_amount = input("Enter new amount: ")

        query = '''UPDATE payments SET amount = %s 
                   WHERE payment_id = %s'''
        params = (new_amount, payment_id)
        threading.Thread(target=execute_query(query, params)).start()
        print("Payment updated successfully!")

    @log_decorator
    def delete_payment(self):
        payment_id = input("Enter the payment ID: ").strip()

        query = "DELETE FROM payments WHERE payment_id = %s"
        params = (payment_id,)
        threading.Thread(target=execute_query(query, params)).start()
        print("Payment deleted successfully!")

    @log_decorator
    def user_statistic(self):
        user_id = input("Enter user ID: ").strip()

        query = '''SELECT COUNT(*) AS total_orders, AVG(amount) AS average_payment, 
                           MAX(amount) AS maximum_payment, MIN(amount) AS minimum_payment
                    FROM payments
                    WHERE user_id = %s'''
        params = (user_id,)
        result = execute_query(query, params)

        if result:
            total_orders, average_payment, maximum_payment, minimum_payment = result[0]
            print(f"Total orders: {total_orders}")
            print(f"Average payment: ${average_payment:.2f}")
            print(f"Maximum payment: ${maximum_payment:.2f}")
            print(f"Minimum payment: ${minimum_payment:.2f}")
        else:
            print("No orders found for the given user.")

    @log_decorator
    def order_statistics(self):
        order_id = input("Enter order ID: ").strip()

        query = '''SELECT COUNT(*) AS total_items, AVG(price) AS average_price, 
                           MAX(price) AS maximum_price, MIN(price) AS minimum_price
                    FROM order_item
                    WHERE order_id = %s'''
        params = (order_id,)
        result = execute_query(query, params)

        if result:
            total_items, average_price, maximum_price, minimum_price = result[0]
            print(f"Total items: {total_items}")
            print(f"Average price: ${average_price:.2f}")
            print(f"Maximum price: ${maximum_price:.2f}")
            print(f"Minimum price: ${minimum_price:.2f}")
        else:
            print("No items found for the given order.")

    @log_decorator
    def financial_reports(self):
        query = '''SELECT SUM(amount), payment_method, COUNT(order_id)
                   FROM payments 
                   GROUP BY payment_method;
                '''
        result = execute_query(query)

        if result:
            print("Financial reports:")
            for total_amount, payment_method, order_count in result:
                print(
                    f"Payment Method: {payment_method}, Total Amount: ${total_amount:.2f}, Number of Orders: {order_count}")
        else:
            print("No payments found.")
