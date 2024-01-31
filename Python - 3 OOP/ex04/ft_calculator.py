class calculator:
    """Class calculator"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate dotproduct"""
        result = sum([x * y for x, y in zip(V1, V2)])
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Calculate add vector"""
        result = [float(x) + float(y) for x, y in zip(V1, V2)]
        print(f"Sum vector is: {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Calculate sous vector"""
        result = [float(x) - float(y) for x, y in zip(V1, V2)]
        print(f"Difference vector is: {result}")
