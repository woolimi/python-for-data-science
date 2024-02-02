from abc import ABC, abstractmethod


class Character(ABC):
    """[Abstract] Character class"""
    @abstractmethod
    def __init__(self, first_name: str, is_alive=True):
        """Character __init__ method"""
        pass

    def die(self):
        """Character __die__ method"""
        self.is_alive = False

    @abstractmethod
    def __str__(self):
        """Character __str__ method"""
        pass

    @abstractmethod
    def __repr__(self):
        """Character __repr__ method"""
        pass


class Stark(Character):
    """Stark Class"""
    def __init__(self, first_name: str, is_alive=True):
        """Stark __init__ method"""
        self.first_name = first_name
        self.is_alive = is_alive
