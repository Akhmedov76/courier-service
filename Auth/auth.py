import datetime
import hashlib

SUPERADMIN_LOGIN = "superadmin"
SUPERADMIN_PASSWORD = "password"


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

        email: str = input("Email: ").strip()
        password: str = hashlib.sha256(input("Password: ").strip().encode('utf-8')).hexdigest()

        if email == SUPERADMIN_LOGIN and password == hashlib.sha256(SUPERADMIN_PASSWORD.encode('utf-8')).hexdigest():
            return {'is_login': True, 'role': 'super_admin'}

        query = '''
        SELECT * FROM USERS WHERE email=%s AND password=%s
        '''
        params = (email, password)
        user = execute_query(query, params, fetch='one')
        if user is None:
            query = '''
                    SELECT * FROM MANAGER WHERE email=%s AND password=%s
            '''
            params = (email, password)
            user = execute_query(query, params, fetch='one')
            if user is None:
                print("Login failed")
                return {'is_login': False, 'role': 'admin'}
        return {'is_login': True, 'role': 'user'}


    def logout(self):
        """
                Set the login status of all users to False (i.e., log out all users).
        """
        self.create_user_table()
        query = 'UPDATE users SET IS_LOGIN=FALSE;'
        with self.__database as db:
            db.execute(query)
            return True
