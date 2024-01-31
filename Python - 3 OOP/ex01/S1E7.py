from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name: str, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Baratheon die method"""
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name: str, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Lannister die method"""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name: str, is_alive=True):
        """Lannister create_lannister method"""
        instance = cls(first_name)
        instance.is_alive = is_alive
        return instance
