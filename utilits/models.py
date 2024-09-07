from database_config.db_settings import execute_query


def create_tables():
    create_users_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(50) UNIQUE NOT NULL,
        phone_number BIGINT UNIQUE NOT NULL,
        password VARCHAR(50) NOT NULL,
        adress VARCHAR(50) NOT NULL,
        role VARCHAR(50) DEFAULT 'USER'
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

    create_delivery_table = ''' 
        CREATE TABLE IF NOT EXISTS delivery (
            id SERIAL PRIMARY KEY,
            order_id INTEGER REFERENCES orders(id),
            courier_id INTEGER REFERENCES couriers(id),
            assigned_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            delivery_date TIMESTAMP
        ); 
    '''

    create_order_table = '''
    CREATE TABLE IF NOT EXISTS orders(
    id SERIAL PRIMARY KEY<
    order_date TIMESTAMP NOT NULL,
    total_amount BIGINT NOT NULL,
    status VARCHAR(50) DEFAULT FALSE,
    user_id INTEGER REFERENCES users(id),
    restaurant_id INTEGER REFERENCES restaurants(id),
    branch_id INTEGER REFERENCES branches(id),

    ); '''

    create_order_item_table = ''' 
    CREATE TABLE IF NOT EXISTS order_item(
    order_id INTEGER REFERENCES orders(id),
    id SERIAL PRIMARY KEY,
    kitchen_menu_id INTEGER REFERENCES kitchen_menu(id)
    quantity BIGINT NOT NULL,
    PRICE DECIMAL NOT NULL
    ); '''


    create_branches_table = '''
    CREATE TABLE IF NOT EXISTS branches (
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(50) NOT NULL,
    adress VARCHAR(50) NOT NULL,
    phone_number BIGINT NOT NULL,
    restaurant_id INTEGER REFERENCES restaurants(id),
    manager_id INTEGER REFERENCES users(id)
    ); '''

    create_payments_table = '''
    CREATE TABLE IF NOT EXISTS payment (
        id SERIAL PRIMARY KEY NOT NULL,
        order_id INTEGER REFERENCES orders(id),
        payments_date TIMESTAMP NOT NULL,
        amount BIGINT NOT NULL,
        payment_method BIGINT NOT NULL
    ); '''


    execute_query(create_users_table)
    execute_query(create_couriers_table)
    execute_query(create_restaurants_table)
    execute_query(create_delivery_table)
    execute_query(create_kitchen_menu_table)
    execute_query(create_order_table)
    execute_query(create_order_item_table)
    execute_query(create_branches_table)
    execute_query(create_payments_table)
