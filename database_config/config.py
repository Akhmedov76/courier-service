import os

from dotenv import load_dotenv


def config(env_file='.env'):
    load_dotenv(env_file)

    db = {
        "database": os.getenv('DB_NAME'),
        "user": os.getenv('DB_USER'),
        "password": os.getenv('DB_PASSWORD'),
        "host": os.getenv('DB_HOST'),
        "port": os.getenv('DB_PORT')
    }

    if None in db.values():
        raise Exception("Missing configuration values in .env file.")
    return db
