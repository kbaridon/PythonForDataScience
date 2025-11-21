from load_image import ft_load
from PIL import Image
import numpy as np


def ft_zoom(path: str, x: int, y: int) -> np.ndarray:
    """Take a path to an image, a x and y coordonate.
    Return a zoom of the image given."""
    img = ft_load(path)
    h, w, _ = img.shape
    if (x + 400 >= w or y + 400 >= h):
        raise AssertionError("bad parameters")

    img = img[y:y+400, x:x+400, 1]
    print("The shape of image is:", img.shape)

    return img


def ft_rotate(path: str) -> np.ndarray:
    """Take a path to an image.
    Cut a square in it, return it by 90° and return it"""
    img = ft_zoom(path, 450, 100)
    print(img)
    transposed = np.empty((img.shape[1], img.shape[0]), dtype=img.dtype)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            transposed[j, i] = img[i, j]
    print("New shape after Transpose:", transposed.shape)
    Image.fromarray(transposed).show()
    return (transposed)


def main():
    """Tester for rotate function"""
    print("Animal:", ft_rotate("animal.jpeg"))
    print("=================")
    print("Fail:", ft_rotate("noting"))


if __name__ == "__main__":
    main()
