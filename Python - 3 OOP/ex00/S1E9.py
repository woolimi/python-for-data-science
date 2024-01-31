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


class Stark(Character):
    """Stark Class"""
    def __init__(self, first_name: str, is_alive=True):
        """Stark __init__ method"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Stark die method"""
        self.is_alive = False
