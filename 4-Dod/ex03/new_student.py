import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate an random id and return it in a string"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Representing the dataclass Student"""
    name: str = field(default="name")
    surname: str = field(default="surname")
    active: bool = field(default=True)
    login: str = field(default="Eagle")
    id: str = field(init=False)

    def __post_init__(self):
        """Init the id wih generate_id"""
        self.id = generate_id()


def main():
    """Tester of generate_id function"""
    student = Student(name="Edward", surname="agle")
    print(student)
    print("-----")
    try:
        student = Student(name="Edward", surname="agle", id="toto")
        print(student)
    except TypeError:
        raise


if __name__ == "__main__":
    main()
