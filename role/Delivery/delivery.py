import threading 
from datetime import datetime
from decorator.decorator import log_decorator 
from database_config.db_settings import execute_query


class Delivery:
    @log_decorator
    def add_delivery(self):
        order_id = input("Enter order ID: ")
        courier_id = input("Enter courier ID: ")
        assigned_time = datetime.now()
        delivery_date = input("Enter delivery date (YYYY-MM-DD HH:MM:SS): ")

        query = '''INSERT INTO delivery (order_id, courier_id, assigned_time, delivery_date) 
                                            VALUES (%s, %s, %s, %s)'''
        params = (order_id, courier_id, assigned_time, delivery_date)
        threading.Thread(target=execute_query(query, params)).start()
        print("Delivery added successfully!")

    @log_decorator
    def update_delivery(self):
        delivery_id = input("Enter the delivery ID: ").strip()
        new_courier_id = input("Enter new courier ID: ")

        query = '''UPDATE delivery SET courier_id = %s 
            WHERE delivery_id = %s'''
        params = (new_courier_id, delivery_id)
        threading.Thread(target=execute_query(query, params)).start()
        print("Delivery updated successfully!")

    @log_decorator
    def delete_delivery(self):
        delivery_id = input("Enter the delivery ID: ").strip()

        query = "DELETE FROM delivery WHERE delivery_id = %s"
        params = (delivery_id,)
        threading.Thread(target=execute_query(query, params)).start()
        print("Delivery deleted successfully!")


    @log_decorator
    def add_courier(self):
        name = input("Enter courier's name: ")
        phone_number = input("Enter courier's phone number: ")
        vehicle_type = input("Enter courier's vehicle type: ")
        current_location = input("Enter courier's current location: ")
        user_id = input("Enter user ID: ")

        query = '''INSERT INTO couriers (name, phone_number, vehicle_type, current_location, user_id) 
                   VALUES (%s, %s, %s, %s, %s)'''
        params = (name, phone_number, vehicle_type, current_location, user_id)
        threading.Thread(target=execute_query(query, params)).start()
        print("Courier added successfully!")

    @log_decorator
    def update_courier_table(self):
        courier_id = input("Enter the courier ID: ").strip()
        new_name = input("Enter new courier's name: ")
        new_phone_number = input("Enter new courier's phone number: ")
        new_vehicle_type = input("Enter new courier's vehicle type: ")
        new_current_location = input("Enter new courier's current location: ")

        query = '''UPDATE couriers SET name = %s, phone_number = %s, vehicle_type = %s, current_location = %s 
                   WHERE courier_id = %s'''
        params = (new_name, new_phone_number, new_vehicle_type, new_current_location, courier_id)
        threading.Thread(target=execute_query(query, params)).start()
        print("Courier updated successfully!")

    @log_decorator
    def delete_courier_table(self):
        courier_id = input("Enter the courier ID: ").strip()

        query = "DELETE FROM couriers WHERE courier_id = %s"
        params = (courier_id,)
        threading.Thread(target=execute_query(query, params)).start()
        print("Courier deleted successfully!")

    @log_decorator
    def get_couriers_by_restaurant(self):
        id = input("Enter restaurant ID: ").strip()
        query = "SELECT * FROM couriers WHERE restaurant_id = %s"
        params = (id,)
        threading.Thread(target=execute_query(query, params, fetch='all')).start()
        print("Couriers retrieved successfully!")
