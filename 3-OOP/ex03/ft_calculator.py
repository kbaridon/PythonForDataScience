class calculator:
    """A very basic calculator class"""

    def __init__(self, vector):
        """Constructor of calculator class"""
        self.vector = vector

    def __add__(self, object) -> None:
        """Scalar operator add (+)"""
        self.vector = [item + object for item in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Scalar operator mul (*)"""
        self.vector = [item * object for item in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Scalar operator sub (-)"""
        self.vector = [item - object for item in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Scalar operator div (/)"""
        if (object == 0):
            raise ZeroDivisionError
        self.vector = [item / object for item in self.vector]
        print(self.vector)


def main():
    """Tester of Calculator class"""
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5
    print("---")
    try:
        v4 = calculator([1.0, 2.0, 3.0])
        v4 / 0
    except ZeroDivisionError:
        raise AssertionError("bad parameters (division by 0)") from None


if __name__ == "__main__":
    main()
