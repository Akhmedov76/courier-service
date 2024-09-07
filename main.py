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
            pass
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
                pass
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


if __name__ == '__main__':
    threading.Thread(target=tables.create_all_table).start()
    threading.Thread(target=auth.logout).start()
    view_auth_menu()
