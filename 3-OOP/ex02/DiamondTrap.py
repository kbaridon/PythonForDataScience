from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the King autority."""

    def __init__(self, first_name, is_alive=True):
        """Constructor for King class"""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color: str):
        """Setter for King eyes"""
        self.eyes = color

    def set_hairs(self, color: str):
        """Setter for King hairs"""
        self.hairs = color

    def get_eyes(self):
        """Getter for King eyes"""
        return self.eyes

    def get_hairs(self):
        """Getter for King hairs"""
        return self.hairs


def main():
    """Tester of King class"""
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)


if __name__ == "__main__":
    main()
