def NULL_not_found(object):
    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif type(object) is float and object != object:
        print(f"Cheese: {object} {type(object)}")
    elif type(object) is int and not object:
        print(f"Zero: {object} {type(object)}")
    elif type(object) is str and not object:
        print(f"Empty: {type(object)}")
    elif type(object) is bool and not object:
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not Found")
        return 1
    return 0
