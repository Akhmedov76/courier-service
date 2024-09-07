import threading

from utilits.models import CreateTable
from Auth.auth import Auth

auth = Auth()
tables = CreateTable()


def view_auth_menu():
    print('''
1. Register
2. Login
3. Logout
    ''')
    try:
        user_input: int = int(input("Choose menu: "))
        if user_input == 1:
            if auth.register():
                view_auth_menu()
            view_auth_menu()
        elif user_input == 2:
            result_login = auth.login()
            if not result_login['is_login']:
                view_auth_menu()
            elif result_login['role'] == 'super_admin':
                admin_menu()
            elif result_login['role'] == 'admin':
                pass
            elif result_login['role'] == 'manager':
                pass
            elif result_login['role'] == 'user':
                user_menu()
        elif user_input == 3:
            print("Good bye!")
            if Auth.logout:
                exit()
            view_auth_menu()
        else:
            print("Invalid input")
            view_auth_menu()
    except Exception as e:
        print(f'Error: {e}')
        view_auth_menu()


def admin_menu():
    print("""
    salom
    """)


def user_menu():
    print("\n--- User Menu ---")


def view_order_menu():
    print("\n--- Manage Orders ---")
    print("""
1. Add Order
2. View Orders
3. Update Order
4. Delete Order
5. Exit
""")
    choice: int = int(input("Choose an action: "))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        print("Exiting...")
        view_auth_menu()
    else:
        print("Invalid choice!")
        view_order_menu()


def view_couriers_menu():
    print("\n--- Manage Couriers ---")
    print("""
    1. Add Courier
    2. View Couriers
    3. Update Courier
    4. Delete Courier
    5. Exit
    """)
    choice: int = int(input("Choose an action: "))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        print("Exiting...")
        view_auth_menu()
    else:
        print("Invalid choice!")
        view_couriers_menu()


def view_restaurants_menu():
    print("\n--- Manage Restaurants ---")
    print("""
    1. Add Restaurant
    2. View Restaurants
    3. Update Restaurant
    4. Delete Restaurant
    5. Exit
    """)
    choice: int = int(input("Choose an action: "))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        print("Exiting...")
        view_auth_menu()
    else:
        print("Invalid choice!")
        view_restaurants_menu()


def view_branches_menu():
    print("\n--- Manage Branches ---")
    print("""
    1. Add Branch
    2. View Branches
    3. Update Branch
    4. Delete Branch
    5. Exit
    """)
    choice: int = int(input("Choose an action: "))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        print("Exiting...")
        view_auth_menu()
    else:
        print("Invalid choice!")
        view_branches_menu()


def view_kitchen_menu():
    print("\n--- Manage Kitchen ---")
    print("""
    1. Add Kitchen
    2. View Kitchens
    3. Update Kitchen
    4. Delete Kitchen
    5. Exit
    """)
    choice: int = int(input("Choose an action: "))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        print("Exiting...")
        view_auth_menu()
    else:
        print("Invalid choice!")
        view_kitchen_menu()


def view_order_items_menu():
    print("\n--- Manage Order Items ---")
    print("""
    1. Add Order Item
    2. View Order Items
    3. Update Order Item
    4. Delete Order Item
    5. Exit
    """)
    choice: int = int(input("Choose an action: "))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        print("Exiting...")
        view_auth_menu()
    else:
        print("Invalid choice!")
        view_order_items_menu()


def view_delivery_menu():
    print("\n--- Manage Deliveries ---")
    print("""
    1. Add Delivery
    2. View Deliveries
    3. Update Delivery
    4. Delete Delivery
    5. Exit
    """)
    choice: int = int(input("Choose an action: "))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        print("Exiting...")
        view_auth_menu()
    else:
        print("Invalid choice!")
        view_delivery_menu()


def view_payment_menu():
    print("\n--- Manage Payments ---")
    print("""
    1. Add Payment
    2. View Payments
    3. Update Payment
    4. Delete Payment
    5. Exit
    """)
    choice: int = int(input("Choose an action: "))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        print("Exiting...")
        view_auth_menu()
    else:
        print("Invalid choice!")
        view_payment_menu()


if __name__ == '__main__':
    threading.Thread(target=tables.create_all_table).start()
    threading.Thread(target=auth.logout).start()
    view_auth_menu()
