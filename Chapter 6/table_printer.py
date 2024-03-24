# table_printer.py - a program to print tables in a formatted way

def print_table(data):
    """Prints a table with right justified columns."""
    # Creates a list of column widths, set to 0.
    col_widths = [0] * len(data)
    # Loops through row in data
    for i in range(len(data)):
        # max width variable
        max_width = 0
        # Loops through each word in row
        for j in range(len(data[i])):
            # If len is greater than max, set max to len
            if len(data[i][j]) > max_width:
                max_width = len(data[i][j])
        # add max width to column widths
        col_widths[i] = max_width

    # prints table columns rjusted to max width of that column.
    # Loops through each column.
    for i in range(len(data[0])):
        # Loops through each row
        for j in range(len(data)):
            # prints word rjusted with a space at the end
            print(data[j][i].rjust(col_widths[j]), end=' ')
        # Moves to next row
        print()


def main():
    """Main method to test print_table() method."""
    table_data = [['apples', 'oranges', 'cherries', 'banana'],
                  ['Alice', 'Bob', 'Carol', 'David'],
                  ['dogs', 'cats', 'moose', 'goose']]
    print_table(table_data)

# If program is run (and not imported), call main() method.
if __name__ == '__main__':
    main()
