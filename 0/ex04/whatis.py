import sys

argc = len(sys.argv)

if argc == 1:
    sys.exit()

if argc > 2:
    print("AssertionError: more than one argument is provided")
    sys.exit()

try:
    num = int(sys.argv[1])
except ValueError:
    print("AssertionError: argument is not an integer")
    sys.exit()

print("I'm Even." if num % 2 == 0 else "I'm Odd.")
