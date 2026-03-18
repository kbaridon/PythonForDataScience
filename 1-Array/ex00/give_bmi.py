def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Take an array (list) and a limit (int).
    Return an array of booleans, True if value > limit, false either way."""
    return [True if val > limit else False for val in bmi]


def bad_args(height: list[int | float], weight: list[int | float]) -> bool:
    """Take two arrays and check arguments of these arrays.
    Return true if a value is negative, null or not a float or a integer."""
    for h, w in zip(height, weight):
        if (not (isinstance(h, (float, int)) and isinstance(w, (float, int)))):
            return True
        if (h <= 0 or w <= 0 or h != h or w != w):
            return True
    return False


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Take an array of height, and an array of weight.
    Return an array of the BMI of theses values.
    Arrays must be the same lenght and have valid arguments."""
    if (len(height) != len(weight) or bad_args(height, weight)):
        raise AssertionError("bad arguments")
    return [w / (h * h) for w, h in zip(weight, height)]


def main():
    """Tester of give_bmi and apply_limit functions"""
    height = [1.58, 2.44]
    weight = [60, 70]

    bmi = give_bmi(height, weight)

    print(bmi)
    print(apply_limit(bmi, 20))

    height[1] = 's'

    # TEST 1: not a float or an integer
    try:
        bmi = give_bmi(height, weight)
        print(bmi)
        print(apply_limit(bmi, 20))
    except AssertionError:
        print("Bad arguments: Test 1")

    height[1] = 2.44
    weight[1] = 0.0

    # TEST 2: null value
    try:
        bmi = give_bmi(height, weight)
        print(bmi)
        print(apply_limit(bmi, 20))
    except AssertionError:
        print("Bad arguments: Test 2")


if __name__ == "__main__":
    main()
