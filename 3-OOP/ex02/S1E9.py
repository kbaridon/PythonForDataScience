from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class representing a Character"""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Constructor for Character"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Method that set to false Character is_alive parameter"""
        self.is_alive = False


class Stark(Character):
    """Class representing a Stark Character"""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Stark class"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Method that set to false Stark is_alive parameter"""
        self.is_alive = False


def main():
    """Tester of Stark and Character classes"""
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)
    print("---")
    try:
        hodor = Character("hodor")
        print(hodor.__dict__)
    except TypeError:
        raise AssertionError("bad parameters") from None


if __name__ == "__main__":
    main()
