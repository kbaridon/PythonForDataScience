import sys


def count_char(str: str) -> dict:
    """Intern function of main().
    Go through the string given by main():
    Count the numbers of characters of each type.
    """
    result = {"total": 0, "up": 0, "low": 0, "punc": 0, "space": 0, "digit": 0}
    i = 0
    while (i < len(str)):
        if (str[i].isspace()):
            result["space"] += 1
        elif (str[i].isdigit()):
            result["digit"] += 1
        elif (str[i].islower()):
            result["low"] += 1
        elif (str[i].isupper()):
            result["up"] += 1
        else:
            result["punc"] += 1
        i += 1
    result["total"] = i
    return (result)


def main():
    """Receive a string and give details about it:
    - Numbers of upper and lower characters
    - Numbers of punctiuation marks
    - Numbers of spaces
    - Numbers of digits"""
    str = ""
    if (len(sys.argv) == 1):
        str = input("Please enter a phrase: ")
    if (len(sys.argv) > 2):
        raise AssertionError("more than one argument is provided")
    if (str == ""):
        str = sys.argv[1]
    value = count_char(str)

    print("The text contains", value["total"], "characters")
    print(value["up"], "upper letters")
    print(value["low"], "lower letters")
    print(value["punc"], "punctuation marks")
    print(value["space"], "spaces")
    print(value["digit"], "digits")


if __name__ == "__main__":
    main()
