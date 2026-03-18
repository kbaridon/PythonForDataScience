import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """Take the path of an image.
    Return the format and pixels content in RGB format."""
    try:
        img = Image.open(path, mode="r")
    except FileNotFoundError:
        raise AssertionError("bad arguments") from None
    if (img.mode != "RGB"):
        img = img.convert("RGB")

    arr = np.asarray(img)
    print("The shape of image is:", arr.shape)
    return (arr)


def main():
    """Tester for ft_load function"""
    print("Animal:", ft_load("animal.jpeg"))
    print("======================")
    print("Landscape:", ft_load("landscape.jpg"))
    print("======================")
    print("Fail:", ft_load("Nothing ahah"))


if __name__ == "__main__":
    main()
