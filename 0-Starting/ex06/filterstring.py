import sys
from ft_filter import ft_filter


def make_append():
    """Anonymous function: append a char in a string."""
    return lambda s, c: s + c


def is_greater(word: str):
    """Take a string a retrun if the string is greater than
    the second argument (argv)."""
    n = int(sys.argv[2])
    return (len(word) > n)


def splitWords(str: str) -> list:
    """Take a string and return a tab of the words of the string"""
    result = []
    append = make_append()
    i = 0
    while (i < len(str)):
        item = ""
        while (i < len(str) and str[i].isspace()):
            i += 1
        while (i < len(str) and not str[i].isspace()):
            item = append(item, str[i])
            i += 1
        result.append(item)
    return (result)


def main():
    """Take two arguments: a string and an integer.
    It then output a list of the words of the string.
    The words have a length greater than the integer"""
    if (len(sys.argv) != 3):
        raise AssertionError("the arguments are bad")
    try:
        tab = splitWords(sys.argv[1])
        result = list(ft_filter(is_greater, tab))
        print(result)
    except ValueError:
        raise AssertionError("the arguments are bad") from None


if __name__ == "__main__":
    main()
