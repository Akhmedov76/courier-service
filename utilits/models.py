from database_config.db_settings import execute_query


def create_tables():
    create_users_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(50) UNIQUE NOT NULL,
        phone_number BIGINT UNIQUE NOT NULL,
        password VARCHAR(50) NOT NULL,
        address VARCHAR(50) NOT NULL,
        role VARCHAR(50) NOT NULL
    ); '''

    create_couriers_table = '''
    CREATE TABLE IF NOT EXISTS couriers (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        phone_number BIGINT UNIQUE NOT NULL,
        vehicle_type VARCHAR(50) NOT NULL,
        current_location VARCHAR(50) NOT NULL,
        user_id BIGINT UNIQUE NOT NULL
    ); '''

    create_restaurants_table = '''
    CREATE TABLE IF NOT EXISTS restaurants (
        id BIGSERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL,
        description VARCHAR(200) NOT NULL,
        phone_number BIGINT UNIQUE NOT NULL,
        adress VARCHAR(50) NOT NULL,
        logo VARCHAR(50) NOT NULL,
        user_id BIGINT UNIQUE NOT NULL
    ); '''

    create_kitchen_menu_table = ''' 
    CREATE TABLE IF NOT EXISTS kitchen_menu (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        description VARCHAR(200) NOT NULL,
        price DECIMAL NOT NULL,
        restaurant_id INTEGER REFERENCES restaurants(id));
         '''
    

    create_branches_table = '''
    CREATE TABLE IF NOT EXISTS branches (
        id BIGINT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        address VARCHAR(255),
        phone_number VARCHAR(20),
        restaurant_id BIGINT,
        user_id BIGINT,
        FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
    ); '''

    create_order_table = '''
    CREATE TABLE IF NOT EXISTS orders(
        id SERIAL PRIMARY KEY,
        order_date TIMESTAMP NOT NULL,
        total_amount BIGINT NOT NULL,
        status VARCHAR(50) DEFAULT FALSE,
        user_id INTEGER REFERENCES users(id),
        restaurant_id INTEGER REFERENCES restaurants(id),
        branch_id INTEGER REFERENCES branches(id)

    ); '''


    create_order_item_table = '''
    CREATE TABLE IF NOT EXISTS order_item (
        id BIGINT PRIMARY KEY,
        order_id BIGINT NOT NULL,
        kitchen_id BIGINT NOT NULL,
        quantity BIGINT NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (order_id) REFERENCES orders(id),
        FOREIGN KEY (kitchen_id) REFERENCES kitchen_menu(id)
    ); '''

    create_delivery_table = ''' 
    CREATE TABLE IF NOT EXISTS delivery (
        id SERIAL PRIMARY KEY,
        order_id INTEGER REFERENCES orders(id),
        courier_id INTEGER REFERENCES couriers(id),
        assigned_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        delivery_date TIMESTAMP
    ); '''

    create_payment_table = '''
    CREATE TABLE payments (
        id BIGINT PRIMARY KEY,
        order_id BIGINT NOT NULL,
        payment_date BIGINT NOT NULL,
        amount BIGINT NOT NULL,
        payment_method BIGINT,
        FOREIGN KEY (order_id) REFERENCES orders(id)
    );'''

    execute_query(create_users_table)
    execute_query(create_couriers_table)
    execute_query(create_restaurants_table)
    execute_query(create_kitchen_menu_table)
    execute_query(create_branches_table)
    execute_query(create_order_table)
    execute_query(create_order_item_table)
    execute_query(create_delivery_table)
    execute_query(create_payment_table)
