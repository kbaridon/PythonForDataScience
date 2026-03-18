from typing import Any


def callLimit(limit: int):
    """Outer function to init a limit and callLimiter inner func."""
    count = 0

    def callLimiter(function):
        """Inner func. to init a func. and limit_function inner func."""
        def limit_function(*args: Any, **kwds: Any):
            """Check if the call of the function didn't pass the limit.
            If it's the case, it raise an AssertionError"""
            try:
                nonlocal count
                count += 1
                if count <= limit:
                    function(*args, **kwds)
                else:
                    raise AssertionError("Too much calls")
            except AssertionError:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter


def main():
    """Tester of callLimit function"""
    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")
    for i in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
