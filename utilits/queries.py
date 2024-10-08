import threading
from database_config.db_settings import execute_query
from decorator.decorator import log_decorator


class Database:

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


    @log_decorator
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
    def add_restaurant(self):
        name = input("Enter restaurant's name: ").strip()
        description = input("Enter restaurant's description: ").capitalize().strip()
        phone_number = input("Enter restaurant's phone number: ").strip()
        address = input("Enter restaurant's address: ").capitalize().strip()
        logo = input("Enter restaurant's logo: ")
        manager_id = input("Enter manager ID: ")

        query = '''INSERT INTO restaurants (name, description, phone_number, address, logo, manager_id) 
                   VALUES (%s, %s, %s, %s, %s, %s)'''
        params = (name, description, phone_number, address, logo, manager_id)
        threading.Thread(target=execute_query(query, params)).start()
        print("Restaurant added successfully!")


    @log_decorator
    def update_restaurant(self):
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
    @log_decorator
    def delete_restaurant(self):
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
        manager_id = input("Enter manager ID: ")

        query = '''INSERT INTO branches (name, address, phone_number, restaurant_id, manager_id)
                   VALUES (%s, %s, %s, %s, %s)'''
        params = (name, address, phone_number, restaurant_id, manager_id)
        threading.Thread(target=execute_query(query, params)).start()
        print("Branch added successfully!")


    @log_decorator
    def update_branch(self):
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
    def delete_branch(self):
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
