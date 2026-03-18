def ft_filter(function: callable, iter):
    """Construct an iterator from those elements
    of iterable for which function is true.
    iter may be either a sequence, a container
    which supports iteration, or an iterator.
    If function is None, the identity function
    is assumed, that is, all elements of iterable
    that are false are removed."""
    if (function):
        return (item for item in iter if function(item))
    return (item for item in iter if item)
