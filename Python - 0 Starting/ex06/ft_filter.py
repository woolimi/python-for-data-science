def ft_filter(func, iter):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable
    for which function(item) is true.
    If function is None, return the items that are true.
    """

    if func is None:
        return [i for i in iter if i]
    else:
        return [i for i in iter if func(i)]
