class calculator:
    """A very basic calculator class"""

    def __new__(cls, *args, **kwargs):
        """Constructor of calculator class"""
        raise TypeError("Can't instantiate class calculator.")

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Take 2 vectors and calculate the dot product of them"""
        result = 0
        for i, y in zip(V1, V2):
            result = result + (i * y)
        print("Dot product is :", result)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Take 2 vectors and print the sum of them"""
        result = [float(x + y) for x, y in zip(V1, V2)]
        print("Add Vector is :", result)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Take 2 vectors and print the substraction of them"""
        result = [float(x - y) for x, y in zip(V1, V2)]
        print("Sous Vector is :", result)


def main():
    """Tester of Calculator class"""
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)
    # try:
    #     t = calculator()
    #     t.dotproduct(a, b)
    # except TypeError:
    #     raise AssertionError("bad parameters.")


if __name__ == "__main__":
    main()
