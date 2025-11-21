def ft_filter(function: callable, iter):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if (function):
        return (item for item in iter if function(item))
    return (item for item in iter if item)
