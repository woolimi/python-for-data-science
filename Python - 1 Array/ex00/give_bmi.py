def is_number(value):
    """
    Get value and return
    """
    return isinstance(value, int) or isinstance(value, float)


def give_bmi(height, weight):
    """
    def give_bmi(
        height: list[int | float],
        weight: list[int | float]
    ) -> list[int | float]

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
            if not isinstance(weight[idx], int) and isinstance(weight[idx], float):
                raise Exception("")
            if not isinstance(height[idx], int) and isinstance(height[idx], float):
                raise Exception("")
            bmi = weight[idx] / (height[idx] ** 2)
            res.push(bmi)
        return res

    except Exception as e:
        print(e)

def apply_limit(bmi, limit):
    try:
        if not isinstance(bmi, list):
            raise Exception("bmi should be a list")
    except Exception as e:
        print(e)