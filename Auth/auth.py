import datetime
import hashlib
import threading

from database_config.db_settings import Database, execute_query
from decorator.decorator import log_decorator
from email_sender.email_checker import check_email

SUPERADMIN_LOGIN = "Super"
SUPERADMIN_PASSWORD = "Super"


class Auth:
    def __init__(self):
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").__str__()
        self.__database = Database()

    @log_decorator
    def register(self):
        """
        Registers a new user by collecting their first name, last name,
        generating a username and password, and storing these details in the database.

        Returns:
        - bool: True if the registration is successful.
        """

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
            print(f"An error occurred while registering: {str(e)}")
            return False

    @log_decorator
    def login(self):
        """
        Authenticate a user by checking their email and password.
        Updates the user's login status to True upon successful login.
        """
        try:
            phone_number: str = input("Phone number: ").strip()
            password: str = hashlib.sha256(input("Password: ").strip().encode('utf-8')).hexdigest()

            if phone_number == SUPERADMIN_LOGIN and password == hashlib.sha256(
                    SUPERADMIN_PASSWORD.encode('utf-8')).hexdigest():
                return {'is_login': True, 'role': 'super_admin'}

            query = '''
            SELECT role FROM users WHERE phone_number=%s AND password=%s
            '''
            params = (phone_number, password)
            user = execute_query(query, params, fetch='one')

            if user is None:
                print("Invalid phone_number or password.")
                return {'is_login': False}

            # Correctly update the status for a successful login
            update_query = 'UPDATE users SET status=TRUE WHERE phone_number=%s'
            execute_query(update_query, params=(phone_number,))

            return {'is_login': True, 'role': user['role']}
        except ValueError:
            print("Invalid input. Please try again.")
            return None
        except IndexError:
            print("Email or password is incorrect.")
            return None
        except Exception as e:
            print(f"An error occurred while logging in: {str(e)}")
            return None

    @log_decorator
    def logout(self):
        """
                Set the login status of all users to False (i.e., log out all users).
        """
        query = 'UPDATE users SET status=FALSE;'
        execute_query(query)
        return True
