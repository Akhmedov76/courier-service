import threading
import hashlib
from decorator.decorator import log_decorator
from email_sender.email_checker import check_email
from database_config.db_settings import execute_query


class Manager:
    @log_decorator
    def add_manager(self):
        name = input("Enter name: ").capitalize().strip()
        email = input("Enter email: ").strip()
        phone_number = input("Enter phone number: ").strip()
        address = input("Enter address: ").strip()
        password = hashlib.sha256(input("Password: ").strip().encode('utf-8')).hexdigest()
        role = 'manager'
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
            print(f"An error occurred while adding manager: {str(e)}")
            return False

    def update_manager(self):
        manager_id = input("Enter the manager ID: ").strip()
        new_name = input("Enter new name: ").capitalize().strip()
        new_email = input("Enter new email: ").strip()
        new_phone_number = input("Enter new phone number: ").strip()
        new_address = input("Enter new address: ").strip()
        new_role = 'manager'

        query = '''UPDATE users SET name = %s, email = %s, phone_number = %s, address = %s, role = %s WHERE id = %s'''
        params = (new_name, new_email, new_phone_number, new_address, new_role, manager_id)
        threading.Thread(target=execute_query(query, params)).start()
        print("manager updated successfully!")
        return None

    @log_decorator
    def delete_manager(self):
        manager_id = input("Enter the manager ID: ").strip()

        query = "DELETE FROM users WHERE id = %s"
        params = (manager_id,)
        threading.Thread(target=execute_query(query, params)).start()
        print("Manager deleted successfully!")
        return None
