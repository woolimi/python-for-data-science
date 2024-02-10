from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def _print_image_info(bef: np.ndarray, aft: np.ndarray):
    """
    Print image information before and after operations
    """
    print(np.array(bef))
    print(f"New shape after slicing: {aft.shape}")
    print(np.array(aft))


def _grayscale(img: np.ndarray) -> np.ndarray:
    """
    Convert image array to grayscale
    """
    size = len(img)
    gray_img = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            gray_img[i][j] = [
                int(
                    img[i][j][0] * 0.299
                    + img[i][j][1] * 0.587
                    + img[i][j][2] * 0.114
                )
            ]

    return np.array(gray_img)


def _crop(img: np.ndarray, coord: tuple, size: int) -> np.ndarray:
    """
    Crop image array from coordinates and size
    """
    new_img = [[0 for _ in range(size)] for _ in range(size)]

    for new_x, x in enumerate(range(coord[0], coord[0] + size)):
        for new_y, y in enumerate(range(coord[1], coord[1] + size)):
            new_img[new_y][new_x] = img[y][x]

    return np.array(new_img)


def _transpose(img: np.ndarray) -> np.ndarray:
    """
    Transpose image array
    It's an operation which flips a matrix over its diagonal
    """
    rows, cols = len(img), len(img[0])
    return np.array([[img[j][i] for j in range(rows)] for i in range(cols)])


def main():
    """
    Program to show rotated and grayscale animal image
    """
    try:
        original_image = ft_load("animal.jpeg")
        if original_image is None:
            return
        edited_image = _crop(original_image, (440, 100), 400)
        edited_image = _grayscale(edited_image)
        edited_image = _transpose(edited_image)

        # By default, plt.imshow() will try to scale array data to 0.0~1.0.
        # So we need to change the scale to 0~255.
        plt.imshow(edited_image, cmap='gray', vmin=0, vmax=255)
        plt.axis('on')
        plt.show()
        _print_image_info(original_image, edited_image)

    except Exception as e:
        print("Unexpected error: ", e)


if __name__ == "__main__":
    main()
