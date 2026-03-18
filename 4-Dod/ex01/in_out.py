def square(x: int | float) -> int | float:
    """Take a int or float and return his square. (x**2)"""
    return (x ** 2)


def pow(x: int | float) -> int | float:
    """Take a int or float and return his power. (x**x)"""
    return (x ** x)


def outer(x: int | float, function) -> object:
    """Outer function to init inner and return an usable object"""
    def inner() -> float:
        """Call the function of outer on a nonlocal x."""
        nonlocal x
        x = function(x)
        return x
    return inner


def main():
    """Tester of outer, square and pow functions"""
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if __name__ == "__main__":
    main()
