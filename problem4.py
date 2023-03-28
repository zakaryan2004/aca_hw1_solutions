"""

## Problem 4 ~ Profiling Decorator
[Profiling](https://en.wikipedia.org/wiki/Profiling_(computer_programming)) is a way to measure the performance of the software application
by measuring the resources used (time, memory, etc.) for the particular parts of it.

We want to create a decorator `@profile` that we can use to analyze the functions.

The decorator should write all the logs to a file, separate from the application output.

Each time a function is called in the application, it should write to the file the time, name of the function and how long it took to run it.

### Example 1
```
from time import sleep

@profile
def foo(x):
    sleep(2)
    return x**2


foo(2)
sleep(60)
foo(42)
```

#### Output: (In `performance.log` file)
```
2023-03-11 21:07:51.998617 - foo(2) - 0:00:02.000984
2023-03-11 21:08:54.013414 - foo(42) - 0:00:02.001023
```

"""


from functools import wraps
import time
import logging


def profile(func):
    """
    A decorator that measures the time taken by a function and writes it to a log file.

    Parameters
    ----------
    func : function
        The function to be decorated.

    Returns
    -------
    function
        The decorated function.

    Raises
    ------
    Exception
        If the log file cannot be opened.

    """

    logging.basicConfig(
        filename="performance.log",
        format="%(asctime)s - %(message)s",
        level=logging.INFO,
    )

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        The wrapper function that is called when the decorated function is invoked.

        Parameters
        ----------
        *args : tuple
            The positional arguments passed to the decorated function.
        **kwargs : dict
            The keyword arguments passed to the decorated function.

        Returns
        -------
        object
            The return value of the decorated function.

        """

        start_time = time.monotonic()

        try:
            result = func(*args, **kwargs)
        except Exception as e:
            logging.info(f"{func.__name__} - ERROR: {str(e)}")
            raise

        end_time = time.monotonic()
        time_diff = end_time - start_time
        str_args = [str(repr(arg)) for arg in args]
        str_args.extend([f"{k} = {repr(v)}" for k, v in kwargs.items()])

        logging.info(f'{func.__name__}({", ".join(str_args)}) - {time_diff:.6f}')

        return result

    return wrapper


@profile
def foo(x: float) -> float:
    """
    A function that squares its argument.

    Parameters
    ----------
    x : float
        The number to be squared.

    Returns
    -------
    float
        The square of the input.

    """

    return x**2


@profile
def bar(x: float, y: float) -> float:
    """
    A function that multiples its arguments.

    Parameters
    ----------
    x : float
        The first number.
    y : float
        The second number.

    Returns
    -------
    float
        The multiplication of the inputs.

    """

    return x * y


@profile
def baz(x: str, y: int) -> str:
    """
    A function that multiples its arguments.

    Parameters
    ----------
    x : float
        The first number.
    y : float
        The second number.

    Returns
    -------
    float
        The multiplication of the inputs.

    """

    return y * x


if __name__ == "__main__":
    foo(2)
    foo(3)
    bar(2, y=3)
    bar(x=3, y=4)
    baz(x="Hi", y=3)
    baz("m", 4)
