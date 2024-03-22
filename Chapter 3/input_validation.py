# input_validation.py - improved version of collatz_sequence.py
"""An improved version of the collatz_sequence.py program that validates input first."""

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
    # try-except clause to catch ValueError if user inputs non-integer value.
    try:
        # Value to store user input.
        number = int(input('Enter number:\n'))

        # Checks if number equals 1. If number equals 1, the program exits.
        if number == 1:
            print('You already entered 1, so the program will now exit.')
            sys.exit()

        # Loops over collatz method until value equals 1.
        while number != 1:
            number = collatz(number)

    except ValueError:
        print('Non-integer value detected. You must enter an integer value.\n'
              'This program will now exit.')


# If input_validation.py is run (instead of imported), calls the main method.
if __name__ == '__main__':
    main()
