from utilits.models import create_tables
from Auth.auth import Auth

auth = Auth()


def auth_menu():
    text = '''
1. Register
2. Login
3. Logout
    '''
    print(text)
    try:
        user_input: int = int(input("Choose menu: "))
        if user_input == 1:
            pass
        elif user_input == 2:
            result_login = auth.login()
            if not result_login['is_login']:
                auth_menu()
            elif result_login['role'] == 'super_admin':
                admin_menu()
            elif result_login['role'] == 'admin':
                pass
            elif result_login['role'] == 'manager':
                pass
            elif result_login['role'] == 'user':
                users_menu()
                auth_menu()
        elif user_input == 3:
            print("Good bye!")
            Auth.logout()
        else:
            print("Invalid input")
            auth_menu()
    except Exception as e:
        print(f'Error: {e}')
        auth_menu()


def admin_menu():
    print("""
    salom
    """)


def users_menu():
    print("""
    hello
    """)


def asaas():
    pass


if __name__ == '__main__':
    create_tables()
    auth_menu()
