import sys


def text_counter(text):
    """
    takes a single string argument and print the number of
    upper-case, lower-case, punctuation, spaces and digits
    """
    length = len(text)
    uppers = 0
    lowers = 0
    puncts = 0
    spaces = 0
    digits = 0

    for char in text:
        if char.isupper():
            uppers += 1
        elif char.islower():
            lowers += 1
        elif char.isspace():
            spaces += 1
        elif char.isdigit():
            digits += 1
        elif char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            puncts += 1

    print(f"The text contains {length} characters:")
    print(f"{uppers} upper letters")
    print(f"{lowers} lower letters")
    print(f"{puncts} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """
    Program takes a single string argument
    User is prompted to provide a string if None or nothing is provided.
    Raise AssertionError if more than one argument is provided.
    """

    try:
        if len(sys.argv) == 1:
            print("What is the text to count?")
            text = sys.stdin.readline()
            text_counter(text)
        elif len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        else:
            text_counter(sys.argv[1])

    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")
        exit(1)


if __name__ == "__main__":
    main()
