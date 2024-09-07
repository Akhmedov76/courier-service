import threading

from database_config.db_settings import execute_query


class CreateTable:
    def create_users_table(self):
        """
        Create users table if it doesn't exist
        """
        query = '''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            phone_number BIGINT UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            address VARCHAR(255) NOT NULL,
            status BOOLEAN DEFAULT FALSE,
            role VARCHAR(50) NOT NULL
        )'''
        execute_query(query)
        return True

    def create_couriers_table(self):
        """
        Create couriers table if it doesn't exist
        """
        query = '''
        CREATE TABLE IF NOT EXISTS couriers (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            phone_number BIGINT UNIQUE NOT NULL,
            vehicle_type VARCHAR(50) NOT NULL,
            current_location VARCHAR(50) NOT NULL,
            user_id BIGINT UNIQUE NOT NULL
        )'''
        execute_query(query)
        return True

    def create_restaurants_table(self):
        '''
        Create restaurants table if it doesn't exist
        '''
        query = '''
        CREATE TABLE IF NOT EXISTS restaurants (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE NOT NULL,
            description VARCHAR(200) NOT NULL,
            phone_number BIGINT UNIQUE NOT NULL,
            adress VARCHAR(50) NOT NULL,
            logo VARCHAR(50) NOT NULL,
            user_id BIGINT UNIQUE NOT NULL
            ); '''
        execute_query(query)
        return True

    def create_kitchen_menu_table(self):
        '''
        Create kitchen menu table if it doesn't exist
        '''
        query = ''' 
        CREATE TABLE IF NOT EXISTS kitchen_menu (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            description VARCHAR(200) NOT NULL,
            price DECIMAL NOT NULL,
            restaurant_id INTEGER REFERENCES restaurants(id));
         '''
        execute_query(query)
        return True

    def create_branches_table(self):
        '''
        Create branches table if it doesn't exist
         '''
        query = '''
        CREATE TABLE IF NOT EXISTS branches (
            id BIGINT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            address VARCHAR(255),
            phone_number VARCHAR(20),
            restaurant_id BIGINT,
            user_id BIGINT,
            FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
        ); '''
        execute_query(query)
        return True

    def create_order_table(self):
        '''
        Create orders table if it doesn't exist
         '''
        query = '''
         CREATE TABLE IF NOT EXISTS orders(
             id SERIAL PRIMARY KEY,
             order_date TIMESTAMP NOT NULL,
             total_amount BIGINT NOT NULL,
             status VARCHAR(50) DEFAULT FALSE,
             user_id INTEGER REFERENCES users(id),
             restaurant_id INTEGER REFERENCES restaurants(id),
             branch_id INTEGER REFERENCES branches(id)

         ); '''
        execute_query(query)
        return True

    def create_order_item_table(self):
        '''
        Create order_item table if it doesn't exist
         '''
        query = '''
         CREATE TABLE IF NOT EXISTS order_item (
             id SERIAL PRIMARY KEY,
             order_id BIGINT NOT NULL,
             kitchen_id BIGINT NOT NULL,
             quantity BIGINT NOT NULL,
             price DECIMAL(10, 2) NOT NULL,
             FOREIGN KEY (order_id) REFERENCES orders(id),
             FOREIGN KEY (kitchen_id) REFERENCES kitchen_menu(id)
         ); '''
        execute_query(query)
        return True

    def create_delivery_table(self):
        '''
        Create delivery table if it doesn't exist
         '''
        query = '''
         CREATE TABLE IF NOT EXISTS delivery (
             id SERIAL PRIMARY KEY,
             order_id INTEGER REFERENCES orders(id),
             courier_id INTEGER REFERENCES couriers(id),
             assigned_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
             delivery_date TIMESTAMP
         ); '''
        execute_query(query)
        return True

    def create_payment_table(self):
        '''
        Create payment table if it doesn't exist
         '''
        query = '''
         CREATE TABLE IF NOT EXISTS payments (
             id BIGINT PRIMARY KEY,
             order_id BIGINT NOT NULL,
             payment_date TIMESTAMP NOT NULL,
             amount DECIMAL(10, 2) NOT NULL,
             payment_method BIGINT,
             FOREIGN KEY (order_id) REFERENCES orders(id)
         ); '''
        execute_query(query)
        return True

    def create_all_table(self):
        """
        Create all tables.
        """
        self.create_users_table()
        self.create_couriers_table()
        self.create_restaurants_table()
        self.create_kitchen_menu_table()
        self.create_branches_table()
        self.create_order_table()
        self.create_order_item_table()
        self.create_delivery_table()
        self.create_payment_table()
        return True
