from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Class King"""
    def __init__(self, first_name: str, is_alive=True):
        """King __init__ method"""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """King set_eyes method"""
        self.eyes = color

    def set_hairs(self, color):
        """King set_hairs method"""
        self.hairs = color

    def get_eyes(self):
        """King get_eyes method"""
        return self.eyes

    def get_hairs(self):
        """King get_hairs method"""
        return self.hairs
