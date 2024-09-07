import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S', filename='logs/info_logs.log', filemode='w')

logging = logging.getLogger(__name__)


class FunctionException(Exception):
    def __init__(self, message, *args):
        super().__init__(message, *args)
        self.message = message

    def __str__(self):
        return self.message


def log_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)

            message = f"Function {func.__name__}: args: {args} kwargs: {kwargs}, result: {result} executed successfully."
            logging.info(message)
            return result
        except Exception as e:
            message = f'Function {func.__name__}: {e}'
            logging.exception(message)
            print(FunctionException(message))

    return wrapper
