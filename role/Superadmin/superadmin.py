import hashlib
import threading

from database_config.db_settings import execute_query
from decorator.decorator import log_decorator
from email_sender.email_checker import check_email


class SuperAdmin:

    @log_decorator
    def add_admin(self):
        name = input("Enter name: ").capitalize().strip()
        email = input("Enter email: ").strip()
        phone_number = input("Enter phone number: ").strip()
        address = input("Enter address: ").strip()
        password = hashlib.sha256(input("Password: ").strip().encode('utf-8')).hexdigest()
        role = 'admin'
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
                        INSERT INTO users (name, email, phone_number, password, address, Role)
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
            print(f"An error occurred while adding admin: {str(e)}")
            return False
    @log_decorator
    def update_admin_table(self):
        admin_id = input("Enter the admin ID: ").strip()
        new_name = input("Enter new name: ").capitalize().strip()
        new_email = input("Enter new email: ").strip()
        new_phone_number = input("Enter new phone number: ").strip()
        new_address = input("Enter new address: ").strip()
        new_role = 'admin'

        query = '''UPDATE users SET name = %s, email = %s, phone_number = %s, address = %s, Role = %s WHERE id = %s'''
        params = (new_name, new_email, new_phone_number, new_address, new_role, admin_id)
        threading.Thread(target=execute_query(query, params)).start()
        print("Admin updated successfully!")
        return None

    @log_decorator
    def delete_admin_table(self):
        admin_id = input("Enter the admin ID: ").strip()

        query = "DELETE FROM users WHERE id = %s"
        params = (admin_id,)
        threading.Thread(target=execute_query(query, params)).start()
        print("Admin deleted successfully!")
        return None
