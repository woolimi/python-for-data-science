import numpy as np


def _get_safe_2d_array(array: list) -> list | None:
    """
    get list if it's 2D, otherwise return None
    """

    try:
        np_arr = np.array(array)
        if np_arr.ndim != 2:
            return None

        return np_arr
    except Exception:
        return None


def slice_me(family: list, start: int, end: int) -> list:
    """
    slice family from start to end.
    return empty list if error happens.
    """

    np_arr = None

    try:
        if not isinstance(family, list) \
                or not isinstance(start, int) or not isinstance(end, int):
            raise Exception("Invalid arguments")

        np_arr = _get_safe_2d_array(family)

        if np_arr is None:
            raise Exception("family is not 2D array")

    except Exception as e:
        print(e)
        return []

    print(f"My shape is : {np_arr.shape}")
    print(f"My new shape is : {np_arr[slice(start, end)].shape}")

    return np_arr[slice(start, end)].tolist()
