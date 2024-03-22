# comma_code.py - a program to join list items and return a string.
"""A program to join list items into a formatted string."""

def comma_code(list):
    """Joins list items into a comma separated string."""
    # If list is empty, returns 'List is empty.' string.
    if len(list) == 0:
        return 'List is empty.'

    # Count value counts items added to string.
    # list_string is string returned at end.
    count = 0
    list_string = ''
    # Loops through list
    for item in list:
        # Checks if count equals index value of last item in list
        if count == (len(list) - 1):
            # Adds 'and' followed by space and then last item in list.
            list_string += 'and ' + str(item)
        else:
            # Adds item to list_string followed by comma and space.
            list_string += str(item) + ', '
        # Count increases after every item added to list_string.
        count += 1

    return list_string


def main():
    """Main method to check if comma_code() method is working properly."""
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(comma_code(spam))
    is_empty = []
    print(comma_code(is_empty))

# If program is run (instead of imported), calls main method.
if __name__ == '__main__':
    main()
