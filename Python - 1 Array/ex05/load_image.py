import numpy as np
from PIL import Image
import os


def ft_load(path: str) -> np.ndarray:
    """
    load an image and return array if image info.
    """
    try:
        (_, extension) = os.path.splitext(path)

        if extension != '.jpg' and extension != '.jpeg':
            raise Exception("file extension should be .jpg or .jpeg")
        if not os.path.exists(path):
            raise Exception("file does not exist")
        img = Image.open(path)
        arr = np.array(img)

        print(f"The shape of Image is: {arr.shape}")

        return arr
    except Exception as e:
        print(e)
