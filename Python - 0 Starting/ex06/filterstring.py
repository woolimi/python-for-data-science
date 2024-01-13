from ft_filter import ft_filter
import sys


def str_to_int(s):
    """
    A function that accepts a string and returns as integer
    """
    try:
        return int(s)
    except ValueError:
        raise AssertionError("the arguments are bad")


def main():
    """
    program that accepts two arguments: a string(S), and an integer(N)
    Print a list of words from S that have a length greater than N
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        argv = [a for a in sys.argv]
        string = argv[1]
        number = str_to_int(argv[2])

        result = ft_filter(lambda s: len(s) > number, string.split())
        print(result)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        exit(1)


if __name__ == "__main__":
    main()
