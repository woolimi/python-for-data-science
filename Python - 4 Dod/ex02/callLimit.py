def callLimit(limit: int):
    """
    Wrapper function that return a decorator "callLimiter"    
    """
    count = 0

    def callLimiter(function):
        """
        Decorator function "callLimiter"

        Decorator always get function as parameter and return another function
        to extend function's behavior
        """
        def limit_function(*args, **kwds):
            """
            Function to limit function calls by counting number of calls
            """
            try:
                nonlocal count
                count += 1
                if count <= limit:
                    return function(*args, **kwds)
                else:
                    raise Exception(f"{function} call too many times")
            except Exception as error:
                print("Error:", error)
        return limit_function
    return callLimiter
