def _is_number(value: int | float) -> bool:
    """
    Get value and return
    """
    return isinstance(value, int) or isinstance(value, float)


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Get list of height and weight as arguments, then return list of bmi
    """
    try:
        if not isinstance(height, list):
            raise Exception("height should be a list")
        if not isinstance(weight, list):
            raise Exception("weight should be a list")
        if len(height) != len(weight):
            raise Exception("list of height and weight are different")
        res = []
        for idx in range(len(height)):
            if not _is_number(weight[idx]):
                raise Exception("")
            if not _is_number(height[idx]):
                raise Exception("")
            bmi = weight[idx] / (height[idx] ** 2)
            res.append(bmi)
        return res

    except Exception as e:
        print(e)


def apply_limit(bmi: list[int | float], limit: int | float) -> list[bool]:
    """
    check if bmi is greater than limit
    """
    try:
        if not isinstance(bmi, list):
            raise Exception("bmi should be a list")
        if not _is_number(limit):
            return Exception("limit should be a number")
        return list(map(lambda x: x > limit, bmi))

    except Exception as e:
        print(e)
