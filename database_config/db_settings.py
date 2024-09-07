import psycopg2
from decorator.decorator import log_decorator

from psycopg2.extras import DictCursor

from database_config.config import config


class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        try:
            self.connection = psycopg2.connect(**config())
            self.cursor = self.connection.cursor(cursor_factory=DictCursor)
            return self
        except Exception as e:
            print(f"Connection or cursor creation failed: {e}")
            raise  # Re-raise the exception to propagate it

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            if exc_tb is not None:
                self.connection.rollback()
            else:
                self.connection.commit()
            self.connection.close()

    @log_decorator
    def execute(self, query, params=None):
        """Execute the query (INSERT, UPDATE, DELETE)"""
        if self.cursor:
            self.cursor.execute(query, params)
            self.connection.commit()

    @log_decorator
    def fetchall(self, query, params=None):
        """Fetch many rows from the database"""
        if self.cursor:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()

    @log_decorator
    def fetchone(self, query, params=None):
        """Fetch only one row from the database"""
        if self.cursor:
            self.cursor.execute(query, params)
            return self.cursor.fetchone()


@log_decorator
def execute_query(query, params=None, fetch=None):
    try:
        with Database() as db:
            if fetch == "all":
                return db.fetchall(query, params)
            elif fetch == "one":
                return db.fetchone(query, params)
            else:
                db.execute(query, params)
    except Exception as e:
        print(f"Exception occurred while executing: {e}")
