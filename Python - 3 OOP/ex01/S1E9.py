from abc import ABC, abstractmethod


class Character(ABC):
    """[Abstract] Character class"""
    @abstractmethod
    def __init__(self, first_name: str, is_alive=True):
        """Character __init__ method"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Character __die__ method"""
        pass

    def __str__(self):
        """Character __str__ method"""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        """Character __repr__ method"""
        return self.__str__()


class Stark(Character):
    """Stark Class"""
    def __init__(self, first_name: str, is_alive=True):
        """Stark __init__ method"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Stark die method"""
        self.is_alive = False
