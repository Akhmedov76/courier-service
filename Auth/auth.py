import datetime
import hashlib

from database_config.db_settings import Database, execute_query
from decorator.decorator import log_decorator

SUPERADMIN_LOGIN = "super"
SUPERADMIN_PASSWORD = "super"


class Auth:
    def __init__(self):
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").__str__()
        self.__database = Database()

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
        with self.__database as db:
            db.execute(query)
            return True
