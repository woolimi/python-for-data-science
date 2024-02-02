from abc import ABC, abstractmethod

# Python, unlike other languages, does not natively support interfaces,
# therefore to implement an interface in Python we use the abc module.
# ABCs are very similar to interfaces, the only subtle difference
# Interface
# - can only have abstract methods
# ABC
# - can have concrete methods


class Character(ABC):
    """[Abstract] Character class"""
    @abstractmethod
    def __init__(self, first_name: str, is_alive=True):
        """Character __init__ method"""
        pass

    def die(self):
        """Character __die__ method"""
        self.is_alive = False


class Stark(Character):
    """Stark Class"""
    def __init__(self, first_name: str, is_alive=True):
        """Stark __init__ method"""
        self.first_name = first_name
        self.is_alive = is_alive
