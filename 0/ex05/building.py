import sys


def main():
    """Takes a single string argument and displays the sums of its
    upper-case characters, lower-case characters, punctuation
    characters, digits, and spaces."""
    try:
        argc: int = len(sys.argv)
        if argc > 2:
            print("AssertionError: more than one argument is provided")
            sys.exit()

        text: str = ""
        if argc == 2:
            text = sys.argv[1]

        if argc == 1:
            print("What is the text to count?")
            text = sys.stdin.read()

        char_count: int = len(text)
        upper_count: int = sum(1 for c in text if c.isupper())
        lower_count: int = sum(1 for c in text if c.islower())
        punctuation_count: int = sum(1 for c in text if c in "!\"#$%&'()*+,-./\
:;<=>?@[\\]^_`{|}~)")
        space_count: int = sum(1 for c in text if c.isspace())
        digit_count: int = sum(1 for c in text if c.isdigit())

        print("The text contains {0:d} characters:\n\
        {1:d} upper letters\n\
        {2:d} lower letters\n\
        {3:d} punctuation marks\n\
        {4:d} spaces\n\
        {5:d} digits".format(char_count, upper_count, lower_count,
                             punctuation_count, space_count, digit_count))
    except Exception:
        print("AssertionError")


if __name__ == "__main__":
    main()
