import datetime
import hashlib

from database_config.db_settings import Database, execute_query
from decorator.decorator import log_decorator

SUPERADMIN_LOGIN = "admin"
SUPERADMIN_PASSWORD = "admin"


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
            email: str = input("Email: ").strip()
            password: str = hashlib.sha256(input("Password: ").strip().encode('utf-8')).hexdigest()

            if email == SUPERADMIN_LOGIN and password == hashlib.sha256(
                    SUPERADMIN_PASSWORD.encode('utf-8')).hexdigest():
                return {'is_login': True, 'role': 'super_admin'}

            query = '''
            SELECT * FROM employee WHERE email=%s AND password=%s
            '''
            params = (email, password)
            employee = execute_query(query, params, fetch='one')
            if employee is None:
                query = '''
                SELECT * FROM company WHERE email=%s AND password=%s
                '''
                params = (email, password)
                manager = execute_query(query, params, fetch='one')
                if manager is None:
                    print("Login failed")
                    return None
                else:
                    update_query = 'UPDATE company SET status=TRUE WHERE email=%s'
                    execute_query(update_query, params=(email,))
                    return {'is_login': True, 'role': 'manager'}
            else:
                update_query = 'UPDATE employee SET status=TRUE WHERE email=%s'
                execute_query(update_query, params=(email,))
                return {'is_login': True, 'role': 'employee'}
        except ValueError:
            print("Invalid input. Please try again.")
            return None
        except IndexError:
            print("Email or password is incorrect.")
            return None
        except Exception as e:
            print(f"An error occurred while logging in: {str(e)}")
            return None

    def create_employee_table(self):
        """
        Create an employee table.
        """
        query = """
                    CREATE TABLE IF NOT EXISTS employee (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(255) NOT NULL,
                    last_name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) UNIQUE NOT NULL,
                    phone_number VARCHAR(20) NOT NULL,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    start_time TIMESTAMP NOT NULL,
                    end_time TIMESTAMP,
                    status BOOLEAN DEFAULT FALSE NOT NULL,
                    company BIGINT NOT NULL REFERENCES company(id),
                    hire_date TIMESTAMP DEFAULT DATE_TRUNC('minute', NOW())
                    );
                """
        with self.__database as db:
            db.cursor.execute(query)
            return None

    @log_decorator
    def logout(self):
        """
                Set the login status of all users to False (i.e., log out all users).
        """
        self.create_employee_table()
        query = 'UPDATE employee SET status=FALSE;'
        with self.__database as db:
            db.execute(query)
            return True
