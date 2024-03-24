# regex_strip.py - A regex version of strip() method.

import re

def regex_strip(text, char=''):
    """Strips string of character(s) specified; whitespaces by default."""
    if char == '':
        strip_regex = re.compile(r'^\s*(\S.*\S)\s*$')  # regex
        stripped = strip_regex.findall(text)  # finds all matches
        return stripped[0]  # returns string
    else:
        char_strip_regex = re.compile(char)  # regex with char provided
        # Substitutes char provided in string with blank.
        string = char_strip_regex.sub('', text)
        # Returns string stripped of char
        return string


def main():
    """Main method to check if regex_strip() methods works."""
    # all text below is for testing; can be changed.
    text = 'colors'
    print(regex_strip(text))
    text = ' colors '
    print(regex_strip(text))
    text = ' colors'
    print(regex_strip(text))
    text = 'colors '
    print(regex_strip(text))
    long_text = ' somewhere over the rainbow'
    print(regex_strip(long_text))
    long_text = 'somewhere over the rainbow '
    print(regex_strip(long_text))
    long_text = ' somewhere over the rainbow '
    print(regex_strip(long_text))
    o_text = 'booooooar'
    print(regex_strip(text, char='col'))
    print(regex_strip(o_text, char='o'))
    print(regex_strip(long_text, char='bow'))

# If program is run (and not imported), calls main() method.
if __name__ == '__main__':
    main()
