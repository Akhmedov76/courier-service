from database_config.db_settings import execute_query
from decorator.decorator import log_decorator


class UserManager:
    @log_decorator
    def view_profile(user_id):
        try:

            query = '''
                SELECT name, email, phone_number, address, Role, status
                FROM users
                WHERE id = %s
            '''
            user_data = execute_query(query, params=(user_id,), fetch='one')

            if user_data:
                name, email, phone_number, address, role, status = user_data
                print("\nYour Profile:")
                print(f"Name: {name}")
                print(f"Email: {email}")
                print(f"Phone Number: {phone_number}")
                print(f"Address: {address}")
                print(f"Role: {role.capitalize()}")
                print(f"Status: {'Active' if status else 'Inactive'}")
                return True
            else:
                print("Profile not found.")
                return False

        except Exception as e:
            print(f"Error retrieving profile: {e}")
            return False

    @log_decorator
    def view_my_orders(self):
        try:
            user_id = int(input("Enter your user ID: "))
            query = '''
                SELECT o.id, o.order_date, o.total_amount, o.status, r.name AS restaurant_name
                FROM orders o
                JOIN restaurants r ON o.restaurant_id = r.id
                WHERE o.user_id = %s
                ORDER BY o.order_date DESC
            '''
            orders = execute_query(query, params=(user_id,), fetch='all')

            if not orders:
                print("You have no orders.")
                return

            print("\nYour Orders:")
            for order in orders:
                order_id, order_date, total_amount, status, restaurant_name = order
                print(f"\nOrder ID: {order_id}")
                print(f"Restaurant: {restaurant_name}")
                print(f"Order Date: {order_date}")
                print(f"Total Amount: ${total_amount:.2f}")
                print(f"Status: {status}")

                query = '''
                    SELECT km.name, oi.quantity, oi.price
                    FROM order_item oi
                    JOIN kitchen_menu km ON oi.kitchen_id = km.id
                    WHERE oi.order_id = %s
                '''
                order_items = execute_query(query, params=(order_id,), fetch='all')

                if order_items:
                    print("\nItems:")
                    for item in order_items:
                        item_name, quantity, price = item
                        print(f"- {item_name}: {quantity} x ${price:.2f}")
                        total_amount += quantity * price
                    print(f"\nTotal Amount for this order: ${total_amount:.2f}")
                    print("\nOrder Status: Complete")
                    print("\nThank you for your order!")
                    return True
                else:
                    print("No items for this order.")
                    return False
        except Exception as e:
            print(f"Error retrieving your orders: {e}")
            return False

    @log_decorator
    def make_new_order(self):
        try:
            user_id = int(input("Enter your user ID: "))

            query = "SELECT id, name FROM restaurants"
            restaurants = execute_query(query, fetch='all')

            if not restaurants:
                print("No restaurants available.")
                return

            print("\nAvailable Restaurants:")
            for idx, restaurant in enumerate(restaurants, 1):
                print(f"{idx}. {restaurant[1]}")

            restaurant_choice = int(input("Select a restaurant by number: ")) - 1
            selected_restaurant = restaurants[restaurant_choice]

            query = "SELECT id, name, price FROM kitchen_menu WHERE restaurant_id = %s"
            menu_items = execute_query(query, params=(selected_restaurant[0],), fetch='all')

            if not menu_items:
                print("No menu available for this restaurant.")
                return False

            order_items = []
            total_amount = 0

            print("\nRestaurant Menu:")
            for idx, item in enumerate(menu_items, 1):
                print(f"{idx}. {item[1]} - ${item[2]:.2f}")

            while True:
                menu_choice = int(input("\nSelect a menu item by number (or 0 to finish): "))
                if menu_choice == 0:
                    break

                selected_item = menu_items[menu_choice - 1]
                quantity = int(input(f"Enter quantity for {selected_item[1]}: "))

                order_items.append((selected_item[0], quantity, selected_item[2]))
                total_amount += selected_item[2] * quantity

            if not order_items:
                print("No items selected.")
                return False

            query = '''INSERT INTO orders (order_date, total_amount, status, user_id, restaurant_id)
                       VALUES (NOW(), %s, 'pending', %s, %s) RETURNING id'''
            params = (total_amount, user_id, selected_restaurant[0])
            order_id = execute_query(query, params=params, fetch='one')[0]

            for item_id, quantity, price in order_items:
                query = '''INSERT INTO order_item (order_id, kitchen_id, quantity, price)
                           VALUES (%s, %s, %s, %s)'''
                params = (order_id, item_id, quantity, price)
                execute_query(query, params=params)

            print("Order placed successfully!")
            print(f"Total amount: ${total_amount:.2f}")
            return True

        except Exception as e:
            print(f"Error placing the order: {e}")
            return False

    @log_decorator
    def view_restaurant_menu(self):
        try:

            query = "SELECT id, name, description FROM restaurants"
            restaurants = execute_query(query, fetch='all')

            if restaurants:
                print("\nAvailable Restaurants:")
                for restaurant in restaurants:
                    restaurant_id, restaurant_name, description = restaurant
                    print(f"\nRestaurant: {restaurant_name}")
                    print(f"Description: {description}")

                    query = "SELECT name, description, price FROM kitchen_menu WHERE restaurant_id = %s"
                    menu_items = execute_query(query, params=(restaurant_id,), fetch='all')

                    if menu_items:
                        print("Menu:")
                        for item in menu_items:
                            name, item_description, price = item
                            print(f"- {name}: {item_description} - ${price:.2f}")
                            print("----------------------------------------")
                        return True
                    else:
                        print("No menu available for this restaurant.")
                        return False
            else:
                print("No restaurants available.")
                return False

        except Exception as e:
            print(f"Error retrieving restaurant menu: {e}")
            return False
