def _mean(*args) -> None:
    """Calculate mean value"""
    if len(args) == 0:
        return print("ERROR")

    res = sum(args) / len(args)
    print(f"mean : {res}")


def _median(*args) -> None:
    """Calculate median value"""
    if len(args) == 0:
        return print("ERROR")

    args = sorted(args)
    if len(args) % 2 == 0:
        res = (args[len(args) // 2] + args[len(args) // 2 - 1]) / 2
    else:
        res = args[len(args) // 2]
    print(f"median : {res}")


def _quartile(*args) -> None:
    """Calculate quartile value (25%, 75%)"""
    if len(args) == 0:
        return print("ERROR")

    args = sorted(args)
    n = len(args)

    q1_index = n // 4
    q3_index = q1_index * 3

    print(f"quartile : {[float(args[q1_index]), float(args[q3_index])]}")


def _std(*args) -> None:
    """Calculate standard deviation value"""
    if len(args) == 0:
        return print("ERROR")

    mean = sum(args) / len(args)
    res = (sum([(x - mean) ** 2 for x in args]) / len(args)) ** 0.5
    print(f"std : {res}")


def _var(*args) -> None:
    """Calculate variance value"""
    if len(args) == 0:
        return print("ERROR")

    mean = sum(args) / len(args)
    res = sum([(x - mean) ** 2 for x in args]) / len(args)
    print(f"var : {res}")


def ft_statistics(*args, **kwargs) -> None:
    try:
        if not isinstance(args, tuple):
            raise Exception("Invalid arguments: args")
        if not isinstance(kwargs, dict):
            raise Exception("Invalid arguments: kwargs")
        valid_option = {
            "mean": _mean,
            "median": _median,
            "quartile": _quartile,
            "std": _std,
            "var": _var
        }
        options = kwargs.values()
        for op in options:
            if op in valid_option:
                valid_option[op](*args)
    except Exception as e:
        print(e)
