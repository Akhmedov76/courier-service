import threading
from utilits.models import CreateTable
from Auth.auth import Auth
from utilits.queries import Database
from role.ClientUser.client import UserManager
from role.Admin.admin import Manager
from role.Superadmin.superadmin import SuperAdmin
from role.Delivery.delivery import Delivery
from role.Manager.manager import Food


auth = Auth()
query = Database()
tables = CreateTable()
manager = Manager()
user_manager = UserManager()
sup_admin = SuperAdmin()
delivery = Delivery()
food = Food()


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
                superadmin_menu()
                view_auth_menu()
            elif result_login['role'] == 'admin':
                admin_menu()
            elif result_login['role'] == 'manager':
                pass
            elif result_login['role'] == 'user':
                manage_user_menu()
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
1. Manage manager info
2. Manage restaurant
3. Manage courier
4. Send message
5. Show statistics
6. Back to auth menu
7. Logout
""")

    choice = input("\nEnter your choice!").strip()
    if choice == "1":
        manage_manager_menu()
        admin_menu()
    elif choice == "2":
        manage_restaurants_menu()
    elif choice == "3":
        manage_couriers_menu()
        admin_menu()
    elif choice == "4":
        pass
    elif choice == "5":
        view_reports_menu()
    elif choice == "6":
        print("See you")
        view_auth_menu()
    elif choice == "7":
        print("Logout!")
        view_auth_menu()
    else:
        print("Invalid choice!")
        admin_menu()


def manage_manager_menu():
    print("""
1. Create manager
2. Update manager
3. Delete manager
4. Back to admin menu
""")

    choice = input("\nEnter your choice!").strip()
    if choice == "1":
        manager.add_manager()
        manage_manager_menu()
    elif choice == "2":
        manager.update_manager()
        manage_manager_menu()
    elif choice == "3":
        manager.delete_manager()
        manage_manager_menu()
    elif choice == "4":
        admin_menu()
    else:
        print("Invalid choice!")
        admin_menu()


def manager_menu():
    print("""\nManager menu:
1.Add food
2.Update food 
3.Delete food 
4.Exit
""")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        pass
        manager_menu()
    elif choice == "2":
        pass
        manager_menu()
    elif choice == "3":
        pass
        manager_menu()
    elif choice == "4":
        print("Exiting...")
        view_auth_menu()
    else:
        print("Invalid choice, please try again!")
        manager_menu()

  


def manage_user_menu():
    print("\nUser Menu:")
    print("1. View My profile")
    print("2. View My orders")
    print("3. Make a new Order")
    print("4. View Restaurant Menu")
    print("5. Logout")

    choice = input("Please select menu: ").strip()
    if choice == "1":
        user_manager.view_profile()
        manage_user_menu()
    elif choice == "2":
        user_manager.view_my_orders()
        manage_user_menu()
    elif choice == "3":
        user_manager.make_new_order()
        manage_user_menu()
    elif choice == "4":
        user_manager.view_restaurant_menu()
        manage_user_menu()
    elif choice == "5":
        print("Logout!")
        view_auth_menu()
    else:
        print("Invalid choice!")
        manage_user_menu()


def superadmin_menu():
    print("""
\nSuperadmin menu\n
1.Create admin
2.Update admin
3.Delete admin
4.Show statistics
5.Logout
""")

    choice = input("\nEnter your choice!").strip()
    if choice == "1":
        sup_admin.add_admin()
        superadmin_menu()
    elif choice == "2":
        sup_admin.update_admin_table()
        superadmin_menu()
    elif choice == "3":
        sup_admin.delete_admin_table()
        superadmin_menu()
    elif choice == "4":
        pass
    elif choice == "5":
        print("Logout!")
        view_auth_menu()
    else:
        print("Invalid choice!")
        superadmin_menu()


def manage_orders_menu():
    print("\nManage Orders:")
    print("1. View All Orders")
    print("2. Update Order Status")
    print("3. View Order Details")
    print("4. Back to Admin Menu")

    choice = input("Please select menu: ").strip()
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        print("Goodbye!")
        view_auth_menu()
    else:
        print("Invalid choice!")
        manage_orders_menu()


def manage_restaurants_menu():
    print("\nManage Restaurants and Branches:")
    print("1. Add Restaurant")
    print("2. Update Restaurant Details")
    print("3. Delete Restaurant")
    print("4. Add Branch")
    print("5. Update Branch Details")
    print("6. Delete Branch")
    print("7. Back to Admin Menu")

    choice = input("Please select menu: ").strip()
    if choice == "1":
        query.add_restaurant()
        manage_restaurants_menu()
    elif choice == "2":
        query.update_restaurant()
        manage_restaurants_menu()
    elif choice == "3":
        query.delete_restaurant()
    elif choice == "4":
        query.add_branch()
        manage_restaurants_menu()
    elif choice == "5":
        query.update_branch()
        manage_restaurants_menu()
    elif choice == "6":
        query.delete_branch()
        manage_restaurants_menu()
    elif choice == "7":
        print("Goodbye!")
        admin_menu()
    else:
        print("Invalid choice!")
        manage_restaurants_menu()


def manage_couriers_menu():
    print("\nManage Couriers:")
    print("1. Add Courier")
    print("2. Update Courier Details")
    print("3. Delete Courier")
    print("4. Back to Admin Menu")

    choice = input("Please select menu: ").strip()
    if choice == "1":
        delivery.add_courier()
        manage_couriers_menu()
    elif choice == "2":
        delivery.update_courier()
        manage_couriers_menu()
    elif choice == "3":
        delivery.delete_courier()
        manage_couriers_menu()
    elif choice == "4":
        print("Goodbye!")
        view_auth_menu()
    else:
        print("Invalid choice!")
        manage_couriers_menu()


def view_reports_menu():
    print("\nView Reports and Statistics:")
    print("1. User Statistics")
    print("2. Order Statistics")
    print("3. Financial Reports")
    print("4. Back to Admin Menu")

    choice = input("Please select menu: ").strip()
    if choice == "1":
        query.user_statistic()
        view_reports_menu()
    elif choice == "2":
        query.order_statistics()
        view_reports_menu()
    elif choice == "3":
        query.financial_reports()
        view_reports_menu()
    elif choice == "4":
        print("Goodbye!")
        admin_menu()
    else:
        print("Invalid choice!")
        view_reports_menu()


def manage_payments_menu():
    print("\nManage Payments:")
    print("1. View All Payments")
    print("2. Update Payment Methods")
    print("3. Back to Admin Menu")

    choice = input("Please select menu: ").strip()
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        print("Goodbye!")
        view_auth_menu()
    else:
        print("Invalid choice!")
        manage_payments_menu()


def send_messages_menu():
    print("\nSend Messages and Notifications:")
    print("1. Send Message to Users")
    print("2. Send Message to Couriers")
    print("3. Back to Admin Menu")

    choice = input("Please select menu: ").strip()
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        print("Goodbye!")
        view_auth_menu()
    else:
        print("Invalid choice!")
        send_messages_menu()


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
    2. Update Delivery
    3. Delete Delivery
    4. Exit
    """)
    choice: int = int(input("Choose an action: "))
    if choice == 1:
        delivery.add_delivery()
        view_delivery_menu()
    elif choice == 2:
        delivery.update_delivery()
        view_delivery_menu()
    elif choice == 3:
        delivery.delete_delivery()
        view_delivery_menu()
    elif choice == 4:
        print("Exiting...")
        view_auth_menu()
    else:
        print("Invalid choice!")
        view_delivery_menu()


if __name__ == '__main__':
    threading.Thread(target=tables.create_all_table).start()
    threading.Thread(target=auth.logout).start()
    view_auth_menu()
