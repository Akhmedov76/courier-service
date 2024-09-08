from database_config.db_settings import execute_query
from decorator.decorator import log_decorator


class UserManager:
    @log_decorator
    def view_profile(self):
        try:
            query = '''
                SELECT name, email, phone_number, address, role, status
                FROM users
                WHERE status = True
            '''
            user_data = execute_query(query, fetch='one')

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
            query = '''
                SELECT o.id, o.order_date, o.total_amount, o.status, r.name AS restaurant_name
                FROM orders o
                JOIN restaurants r ON o.restaurant_id = r.id
                WHERE o.status = True
                ORDER BY o.order_date DESC
            '''
            orders = execute_query(query, fetch='all')

            if not orders:
                print("You have no orders.")
                return False

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

            print("Do you want to place an order based on:")
            print("1. Branch")
            print("2. Restaurant")
            choice = int(input("Enter 1 or 2: "))

            if choice == 1:

                query = "SELECT id, name FROM branches"
                branches = execute_query(query, fetch='all')

                if not branches:
                    print("No branches available.")
                    return

                print("\nAvailable Branches:")
                for idx, branch in enumerate(branches, 1):
                    print(f"{idx}. {branch[1]}")

                branch_choice = int(input("Select a branch by number: ")) - 1
                selected_branch = branches[branch_choice]

                query = "SELECT id, name FROM restaurants WHERE branch_id = %s"
                restaurants = execute_query(query, params=(selected_branch[0],), fetch='all')

                if not restaurants:
                    print("No restaurants available for this branch.")
                    return

            elif choice == 2:

                query = "SELECT id, name FROM restaurants"
                restaurants = execute_query(query, fetch='all')

                if not restaurants:
                    print("No restaurants available.")
                    return

            else:
                print("Invalid choice.")
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
                print(f"{idx}. {item[1]} - {item[2]:.2f}")

            while True:
                menu_choice = int(input("\nSelect menu by number (or 0 to finish): "))
                if menu_choice == 0:
                    break

                selected_item = menu_items[menu_choice - 1]
                quantity = int(input(f"Enter quantity for {selected_item[1]}: "))

                order_items.append((selected_item[0], quantity, selected_item[2]))
                total_amount += selected_item[2] * quantity

            if not order_items:
                print("No items selected.")
                return False

            if choice == 1:

                query = '''INSERT INTO orders (order_date, total_amount, status, user_id, restaurant_id, branch_id)
                           VALUES (NOW(), %s, FALSE, %s, %s, %s) RETURNING id'''
                params = (total_amount, user_id, selected_restaurant[0], selected_branch[0])
            else:

                query = '''INSERT INTO orders (order_date, total_amount, status, user_id, restaurant_id)
                           VALUES (NOW(), %s, FALSE, %s, %s) RETURNING id'''
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
        except IndexError:
            print("Error: Invalid selection. Please try again.")
            return False

        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")
            return False
