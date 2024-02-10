import numpy as np
from PIL import Image


def _show_image(array: np.ndarray) -> np.ndarray:
    """
    Shows the image received.
    """
    Image.fromarray(array).show()
    return array


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    if array is None:
        print("Invalid image")
        return None
    img = 255 - array
    return _show_image(img)


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Red color of the image received.
    """
    if array is None:
        print("Invalid image")
        return None
    img = array.copy()
    for row in img:
        for el in row:
            el[1] = 0
            el[2] = 0
    return _show_image(img)


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Green color of the image received.
    """
    if array is None:
        print("Invalid image")
        return None
    img = array.copy()
    for row in img:
        for el in row:
            el[0] = 0
            el[2] = 0
    return _show_image(img)


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Green color of the image received.
    """
    if array is None:
        print("Invalid image")
        return None
    img = array.copy()
    for row in img:
        for el in row:
            el[0] = 0
            el[1] = 0
    return _show_image(img)


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Gray color of the image received.
    """
    if array is None:
        print("Invalid image")
        return None
    img = array.copy()
    for row in img:
        for el in row:
            mean = int(np.mean(el))
            el[0] = mean
            el[1] = mean
            el[2] = mean
    return _show_image(img.astype(np.uint8))
