from load_image import ft_load
from PIL import Image
import numpy as np
import random  # for the main


def ft_invert(array) -> np.ndarray:
    """Invert the color of a 3D array."""
    print("The shape of image is:", array.shape)
    print(array)

    pimpedArray = 255 - array

    print("Inverts the color of the image received.")
    Image.fromarray(pimpedArray).show()
    return pimpedArray


def ft_red(array) -> np.ndarray:
    """Turn the color of a 3D array red."""
    print("The shape of image is:", array.shape)
    print(array)

    red = array[:, :, 0]
    pimpedArray = np.zeros_like(array)
    pimpedArray[:, :, 0] = red

    print("Turn the color red of the image received.")
    Image.fromarray(pimpedArray).show()
    return pimpedArray


def ft_green(array) -> np.ndarray:
    """Turn the color of a 3D array green"""
    print("The shape of image is:", array.shape)
    print(array)

    green = array[:, :, 1]
    pimpedArray = np.zeros_like(array)
    pimpedArray[:, :, 1] = green

    print("Turn the color green of the image received.")
    Image.fromarray(pimpedArray).show()
    return pimpedArray


def ft_blue(array) -> np.ndarray:
    """Turn the color of a 3D array blue"""
    print("The shape of image is:", array.shape)
    print(array)

    blue = array[:, :, 2]
    pimpedArray = np.zeros_like(array)
    pimpedArray[:, :, 2] = blue

    print("Turn the color blue of the image received.")
    Image.fromarray(pimpedArray).show()
    return pimpedArray


def ft_grey(array) -> np.ndarray:
    """Turn the color of a 3D array grey"""
    print("The shape of image is:", array.shape)
    print(array)

    red = array[:, :, 0] / 3
    green = array[:, :, 1] / 3
    blue = array[:, :, 2] / 3
    grey = red + green + blue
    pimpedArray = np.stack([grey, grey, grey], 2)

    print("Turn the color grey of the image received.")
    Image.fromarray(pimpedArray.astype(np.uint8)).show()
    return pimpedArray


def main():
    """Tester for pimp function"""
    arr = ft_load("landscape.jpg")

    rand = random.randint(0, 5)
    if (rand == 1):
        ft_invert(arr)
    elif (rand == 2):
        ft_red(arr)
    elif (rand == 3):
        ft_green(arr)
    elif (rand == 4):
        ft_blue(arr)
    else:
        ft_grey(arr)


if __name__ == "__main__":
    main()
