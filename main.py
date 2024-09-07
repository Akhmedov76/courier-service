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


if __name__ == '__main__':
    threading.Thread(target=tables.create_all_table).start()
    threading.Thread(target=auth.logout).start()
    view_auth_menu()
