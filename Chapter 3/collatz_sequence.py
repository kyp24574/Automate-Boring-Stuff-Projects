# collatz_sequence.py - a collatz sequence program.
"""A Collatz Sequence program designed to calculate the collatz sequence of an integer value."""

import sys

def collatz(number):
    """Calculates the next number in the sequence."""
    if number % 2 == 0:
        even = number // 2
        print(even)
        return even
    else:
        odd = 3 * number + 1
        print(odd)
        return odd


def main():
    """Program to check if collatz() works properly"""
    # Value to store user input.
    number = int(input('Enter number:\n'))

    # Checks if number equals 1. If number equals 1, the program exits.
    if number == 1:
        print('You already entered 1, so the program will now exit.')
        sys.exit()

    # Loops over collatz method until value equals 1.
    while number != 1:
        number = collatz(number)

# If collatz_sequence.py is run (instead of imported), calls the main method.
if __name__ == '__main__':
    main()
