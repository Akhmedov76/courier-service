import threading

from database_config.db_settings import execute_query
from decorator.decorator import log_decorator
from email_sender.email import send_mail


class EmailSendMessage:
    import threading

    import threading

    @log_decorator
    def send_email_all_users(self):

        subject = input("Enter subject: ")
        message = input("Enter message: ")

        query = """
        SELECT email FROM users
        """

        result = execute_query(query, fetch="all")

        if result:
            for row in result:
                email = row['email']
                threading.Thread(target=send_mail, args=(email, subject, message)).start()

            print("Emails sent successfully.")
            return True
        else:
            print("No users found.")
            return False
