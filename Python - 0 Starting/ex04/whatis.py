import sys


def check_odd_even(number):
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


def str_to_int(s):
    try:
        return int(s)
    except ValueError:
        raise AssertionError("argument is not an integer")


def main():
    try:
        if len(sys.argv) == 1:
            exit()
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")

        input = str_to_int(sys.argv[1])
        check_odd_even(input)
    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")


# Main
if __name__ == "__main__":
    main()
