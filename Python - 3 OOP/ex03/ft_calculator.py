class calculator:
    """Class calculator"""

    def __init__(self, vector):
        self.vector = vector

    def __add__(self, object) -> None:
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        if object == 0:
            print("Division by zero error")
        self.vector = [x / object for x in self.vector]
        print(self.vector)
