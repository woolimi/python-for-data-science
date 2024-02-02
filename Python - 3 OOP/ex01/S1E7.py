from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name: str, is_alive=True):
        """Baratheon __init__ method"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __repr__(self):
        """Baratheon __repr__ method"""
        return self.__str__()

    def __str__(self):
        """Baratheon __str__ method"""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name: str, is_alive=True):
        """Lannister __init__ method"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __repr__(self):
        """Lannister __repr__ method"""
        return self.__str__()

    def __str__(self):
        """Lannister __str__ method"""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    # difference between classmethod and staticmethod
    # both classM and staticM can be called without creating an instance
    # however classM can access class information, but not for staticM
    @classmethod
    def create_lannister(cls, first_name: str, is_alive=True):
        """Lannister create_lannister method"""
        instance = cls(first_name)
        instance.is_alive = is_alive
        return instance
