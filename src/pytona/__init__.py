import cProfile
import pstats
import functools
from typing import Callable


def default_filename(func: Callable) -> str:
    return f"{func.__name__}.prof"


def chronograph(_func=None, *, filename=None):
    def clocked_function(func):
        @functools.wraps(func)
        def wrapped_func(*args, filename=filename, **kwargs):
            try:
                with cProfile.Profile() as pr:
                    result = func(*args, **kwargs)
            except TypeError:
                raise TypeError("Provide the filename as a keyword argument to the chronograph decorator.")

            stats = pstats.Stats(pr)
            stats.sort_stats(pstats.SortKey.TIME)

            if filename is None:
                filename = default_filename(func)

            stats.dump_stats(filename=filename)

            return result
        return wrapped_func

    if _func is None:
        return clocked_function
    
    return clocked_function(_func)
