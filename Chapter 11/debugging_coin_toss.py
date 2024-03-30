# debugging_coin_toss.py - A debugged version of coin toss.
import random

def check_guess(guess):
    """Check guess and raise exception if unexpected value is entered."""
    if guess != 'heads' and guess != 'tails':
        raise Exception('Guess must be heads or tails.')


def main():
    """Main method to run coin toss program."""
    # Try-Except clause to catch raised exception should it occur.
    try:
        # Ask user for heads or tails
        guess = input('Guess the coin toss! Enter heads or tails:\n')
        check_guess(guess)  # check guess
        conversion = {0: 'tails', 1: 'heads'}  # convert values
        toss = random.randint(0, 1)  # 0 is tails, 1 is heads
        # If guess matches toss
        if conversion[toss] == guess:
            print('You got it!')
        else:
            # Ask user for guess again
            guess = input('Nope! Guess again!:\n')
            check_guess(guess)  # check guess
            # If guess matches toss.
            if conversion[toss] == guess:
                print('You got it!')
            else:
                print('Nope. You are really bad at this game.')  # end game.
    # Catch exception and print string version of error to screen.
    except Exception as err:  # Exception object is stored in err.
        print('An exception happened: ' + str(err))


if __name__ == '__main__':
    main()
