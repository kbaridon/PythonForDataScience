import sys


def get_value(char):
    """Take a char as a key and return his morse value."""
    NESTED_MORSE = {" ": "/ ", '0': '----- ', '1': '.---- ', '2': '..--- ',
                    '3': '...-- ', '4': '....- ', '5': '..... ', '6': '-.... ',
                    '7': '--... ', '8': '---.. ', '9': '----. ',
                    ',': '--..-- ', '.': '.-.-.- ', 'A': '.- ', 'B': '-... ',
                    'C': '-.-. ', 'D': '-.. ', 'E': '. ', 'F': '..-. ',
                    'G': '--. ', 'H': '.... ', 'I': '.. ', 'J': '.--- ',
                    'K': '-.- ', 'L': '.-.. ', 'M': '-- ', 'N': '-. ',
                    'O': '--- ', 'P': '.--. ', 'Q': '--.- ', 'R': '.-. ',
                    'S': '... ', 'T': '- ', 'U': '..- ', 'V': '...- ',
                    'W': '.-- ', 'X': '-..- ', 'Y': '-.-- ', 'Z': '--.. '}
    return (NESTED_MORSE[char])


def main():
    """Take a string and print the string in morse code."""
    if (len(sys.argv) != 2):
        raise AssertionError("the arguments are bad")
    try:
        str = sys.argv[1]
        result = ""
        for char in str:
            if (char.islower()):
                char = char.upper()
            result = result + get_value(char)
        print(result)
    except KeyError:
        raise AssertionError("the arguments are bad") from None


if __name__ == "__main__":
    main()
