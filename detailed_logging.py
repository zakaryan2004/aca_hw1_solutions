import time
from functools import wraps
import logging

# w = write
# a = append

# NOSET = 0
# DEBUG = 10
# INFO = 20
# WARNING = 30 <-- default
# ERROR = 40
# CRITICAL = 50


# Create a logger
# The name of the logger is the name of the module
# We set a name to the logger because we can have multiple loggers in the same program
# Each logger has a name and we can use that name to filter the messages
# We use the name to know which logger is writing the message
# If we don't set a name, the logger will use the name of the root logger
# The root logger is the logger that is created by default
logger = logging.getLogger(__name__)
# Set the level to debug (or higher) because we want to see all messages by default
logger.setLevel(logging.DEBUG)


# Create a stream handler (console)
c_handler = logging.StreamHandler()

# Set the level to info (or higher) because we don't want to see debug messages in the console
c_handler.setLevel(logging.INFO)

# Create a formatter for the console handler (we can use different formatters for different handlers)
# We want to keep the console output simple and short
# The default format is '%(levelname)s:%(name)s:%(message)s'
# %(name)s shows the name of the logger (we set this above in the getLogger() call)
# %(levelname)s shows the level of the message
# %(message)s shows the message we log using logger.info(), logger.debug(), etc...
c_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
c_handler.setFormatter(c_format)


# Create a file handler
# We can change the mode to 'w' to overwrite the file every time we run the program
# The default mode is 'a' which appends to the file
f_handler = logging.FileHandler("file.log")

# Set the level to debug (or higher) because we want to see all messages in the file
f_handler.setLevel(logging.DEBUG)

# Create a formatter for the file handler
# We want to keep the file output detailed and long
f_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
f_handler.setFormatter(f_format)


# Add handlers to the logger
# We can add multiple handlers to the same logger
#
# The logger will send the messages to all handlers
# The handlers will decide what to do with the messages
# For example, a handler will ignore the message if the message level is lower than the level of the handler
#
# We can use different handlers to send the messages to different destinations
# For example, we can send the messages to the console and to a file (or a database, etc...)
#
logger.addHandler(c_handler)
logger.addHandler(f_handler)


# logger.debug("debug message, only in file")
# logger.info("info message, both file and console")
# logger.warning("warning message, both file and console")


def profile(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.debug(f"Executing decorated function {func.__name__}...")

        start = time.time()
        result = func(*args, **kwargs)
        time_diff = time.time() - start

        logger.debug(
            f"Finished executing decorated function {func.__name__}; result = {result}"
        )

        str_args = [str(repr(arg)) for arg in args]
        str_args.extend([f"{k} = {repr(v)}" for k, v in kwargs.items()])
        str_args = ", ".join(str_args)

        logger.info(f"{func.__name__}({str_args}) - {time_diff:.9f}")

        return result

    return wrapper


@profile
def foo(x: float, y: float) -> float:
    try:
        return x / y
    except ZeroDivisionError as e:
        logger.error(e)
        # We can also log the exception data using the exc_info parameter
        # logger.error(e, exc_info=True)
        # The equivalent of the above is:
        # logger.exception(e)

        # We can also keep the stack trace of the exception
        # logger.error(e, exc_info=True, stack_info=True)
        # The equivalent of the above is:
        # logger.exception(e, stack_info=True)

        # We raise the exception so the other parts of the program can handle it
        # If it's not handled anywhere else, the program will stop executing
        # If that happens, the exception will be printed to the console again
        raise


@profile
def baz(x: str, y: int) -> str:
    return y * x


foo(1, 2)
baz("Hi", 3)
foo(5, 0)
