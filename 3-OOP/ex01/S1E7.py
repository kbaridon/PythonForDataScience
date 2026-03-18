from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive="True"):
        """Constructor for Baratheon class"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Method that set to false Baratheon is_alive parameter"""
        self.is_alive = False

    def __str__(self):
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __repr__(self):
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name, is_alive="True"):
        """Constructor for Lannister class"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Method that set to false Lannister is_alive parameter"""
        self.is_alive = False

    def __str__(self):
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __repr__(self):
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """Create a Lannister with a custom name and is_alive status"""
        return cls(first_name, is_alive)


def main():
    """Tester of Baratheon and Lannister class"""
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")
    Jaine = Lannister.create_lannister("Jaine", True)
    print(f"Name: {Jaine.first_name, type(Jaine).__name__},",
          f"Alive: {Jaine.is_alive}")


if __name__ == "__main__":
    main()
