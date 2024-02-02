class calculator:
    """Class calculator"""

    def __init__(self, vector):
        """Calculator __init__ method"""
        self.vector = vector

    def __add__(self, object) -> None:
        """Calculator __add__ method"""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Calculator __sub__ method"""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Calculator __mul__ method"""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Calculator __truediv__ method"""
        if object == 0:
            print("Division by zero error")
            return
        self.vector = [x / object for x in self.vector]
        print(self.vector)
