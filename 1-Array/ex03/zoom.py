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
    print(img)

    img = img[y:y+400, x:x+400, 1]
    print("New shape after slicing:", img.shape)

    Image.fromarray(img).show()
    return img


def main():
    """Tester of the ft_zoom function"""
    print("Animal:", ft_zoom("animal.jpeg", 450, 100))
    print("=================")
    print("Fail:", ft_zoom("noting", 200, 200))


if __name__ == "__main__":
    main()
