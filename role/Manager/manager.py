import threading
from decorator.decorator import log_decorator
from database_config.db_settings import execute_query
class Food:

    @log_decorator
    def add_food(self):
        try:
            name = input("Enter the name of the food: ").strip()
            description = input("Enter the description: ").strip()
            price = float(input("Enter the price: ").strip())
            restaurant_id = int(input("Enter the restaurant ID: ").strip())

            query = '''
                INSERT INTO kitchen_menu (name, description, price, restaurant_id)
                VALUES (%s, %s, %s, %s)
            '''
            params = (name, description, price, restaurant_id)

            threading.Thread(target=execute_query(query, params=params))
            print(f"'{name}' Food has been successfully added to the menu.")
        
        except Exception as e:
            print(f"Error while adding the food to the menu: {e}")


    @log_decorator     
    def update_food(self):
        try:
            food_name = input("Enter the admin ID: ").strip()
            new_description = input("Enter new name: ").capitalize().strip()
            new_restaurant_id = input("Enter new email: ").strip()

            query = '''UPDATE kitchen_menu SET name = %s,description =%s, restaurant_id =%s  WHERE restaurant_id = %s'''
            params = (food_name,new_description, new_restaurant_id)
            threading.Thread(target=execute_query(query, params)).start()
            print("food updated successfully!")

        except Exception as e:
            print(f"Error while updating food : {e}")

    @log_decorator
    def delete_food(self):
        try:    
            food_name = input("Enter the food name: ").strip()

            query = "DELETE FROM kitchen_menu WHERE name = %s"
            params = (food_name)
            threading.Thread(target=execute_query(query, params)).start()
            print("Food deleted successfully!")

        except Exception as e:
            print(f"Error while adding the food to the menu: {e}")
