import numpy as np  # python -m pip install numpy


def check_size(lst: list) -> bool:
    """Take a 2d array and return if the row are the same size or not."""
    lenght = -1
    if (len(lst) < 1):
        return True
    for row in lst:
        if (lenght == -1):
            lenght = len(row)
        elif (lenght != len(row)):
            return True
    return False


def slice_me(family: list, start: int, end: int) -> list:
    """Take a list, a start and a end index.
    Return a list sliced with start and end. (shaped)"""
    if (type(family) is not list or check_size(family)):
        raise AssertionError("bad arguments")

    arr = np.array(family)
    print("My shape is :", arr.shape)

    sliced = arr[start:end, :]
    print("My new shape is :", sliced.shape)

    return sliced.tolist()


def main():
    """Tester of slice_me function"""
    arr = [[i + 1 for i in range(3)] for j in range(4)]
    print(arr)
    print(slice_me(arr, 0, 2))
    print(slice_me(arr, -1, 478))


if __name__ == "__main__":
    main()
