# coin_flip_streaks.py - A program to calculate the probability of a heads/tails streak in a randomly generated list.
"""This program calculates the probability of a streak of six heads/tails in a randomly generated list."""
import random

def coin_flips():
    """Calculates the probability of streaks in 100000 coin flips"""
    # Variable for number of streaks
    number_of_streaks = 0
    for experiment_number in range(10000):
        # List variable to contain coin flips
        coin_tosses = []
        # Variable to count number of heads/tails in a row
        streak = 1
        for i in range(100):
            # Flips a coin and appends result to coin_tosses
            coin_tosses.append(random.choice(['H','T']))
            # Skips if it's the first coin flip
            if i != 0:
                # Checks if coin flip matches the last coin flip
                if coin_tosses[i] == coin_tosses[i-1]:
                    streak += 1
                else:
                    streak = 1  # Resets if not the same

                # If streak has reached 6, increase the number_of_streaks by one
                if streak == 6:
                    number_of_streaks += 1
                    break  # Breaks out of for loop (100) once a streak is found and moves on to next one.

    # Prints out the probability of streaks.
    print('Chance of streak: %s%%' % (number_of_streaks / 100))


def main():
    """Main method to check if coin_flips() works properly."""
    coin_flips()

# If program is run (and not imported), calls main() method.
if __name__ == '__main__':
    main()
