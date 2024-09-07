from database.db_settings import execute_query

def create_tables():
    create_users_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(50) UNIQUE NOT NULL,
        phone_number BIGINT UNIQUE NOT NULL,
        password VARCHAR(50) NOT NULL,
        adress VARCHAR(50) NOT NULL,
        role VARCHAR (50) DEFAULT USER 
        
    ); '''


    superadmin_login_parol ='''
    INSERT INTO users (
    username,
    password,
    role)
    VALUES ('superadmin', 'superpassword', 'superadmin')
    ON CONFLICT(username) DO NOTHING; '''


    create_couriers_table = '''
    CREATE TABLE IF NOT EXISTS couriers (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        phone_number BIGINT UNIQUE NOT NULL,
        vehicle_type VARCHAR(50) NOT NOLL,
        current_location VARCHAR(50) NOT NULL,
        user_id BIGINT UNIQUE NOT NULL
    ); '''


    create_restaurants_table = '''
    CREATE TABLE IF NOT EXISTS restaurants (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL,
        description VARCHAR(200) NOT NULL,
        phone_number BIGINT UNIQUE NOT NULL,
        adress VARCHAR(50) NOT NILL,
        logo VARCHAR(50) NOT NULL,
        user_id BIGINT UNIQUE NOT NULL
    ); '''


    create_delivery_table = ''' 
    CREATE TABLE IF NOT EXIST delivery (
        id SERIAL PRIMARY KEY,
        order_id INTEGER REFERENCES orders(id),
        courier_id INTEGER REFERENCES couriers(id),
        assigned_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        delivery_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    ); '''

    execute_query(create_users_table)
    execute_query(superadmin_login_parol)
    execute_query(create_couriers_table)
    execute_query(create_restaurants_table)
    execute_query(create_delivery_table)
