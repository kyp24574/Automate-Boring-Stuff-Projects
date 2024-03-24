# strong_password_detection.py - A program to determine if a password is strong.
import re

def password_strength(password):
    """Checks the strength of password passed."""
    # Returns True if all tests passed
    is_strong = False
    length = len(password)  # Length of password
    lower_regex = re.compile(r'[a-z]+')  # regex for lowercase letter
    upper_regex = re.compile(r'[A-Z]+')  # regex for uppercase letter
    num_regex = re.compile(r'\d+')  # regex for digit
    specialchar_regex = re.compile(r'[!@#$%^&*()]')  # regex for special characters

    # If password is not long enough
    if length < 8:
        print('Your password must contain at least 8 characters.')
    # If there are no lower case letters in password
    elif lower_regex.search(password) is None:
        print('Your password must contain at least 1 lowercase letter.')
    # If there are no upper case letters in password
    elif upper_regex.search(password) is None:
        print('Your password must contain at least 1 uppercase letter.')
    # If there are no numbers in password
    elif num_regex.search(password) is None:
        print('Your password must contain at least 1 digit.')
    # If there are no special characters in password
    elif specialchar_regex.search(password) is None:
        print('Your password must contain at least 1 special character.')
    # If all above tests are passed.
    else:
        is_strong = True

    return is_strong


def main():
    """Main method to check password_strength() method."""
    # Test string; can be changed
    password = 'aA8%aaaa'
    strength = password_strength(password)
    if strength:
        print('Your password is strong!')

# If program is run (and not imported), calls main() method.
if __name__ == '__main__':
    main()
