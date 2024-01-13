import sys


def str_to_morse(text):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
        " ": "/",
    }
    try:
        list = [morse_code_dict[char.upper()] for char in text]
        return " ".join(list)
    except KeyError:
        raise AssertionError("the arguments are bad")


def main():
    """
    a program that takes a string as an argument 
    and encodes it into Morse Code.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        print(str_to_morse(sys.argv[1]))

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        exit(1)


if __name__ == "__main__":
    main()
