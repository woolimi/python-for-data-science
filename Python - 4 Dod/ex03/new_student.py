import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate random id"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Student class with dataclass    
    """
    name: str = field()
    surname: str = field()
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        self.login = self.name[0].capitalize() + self.surname
