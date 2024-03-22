# character_picture_grid.py - a program to rotate grid clockwise 90 degrees.
"""Program to print a list within a list in a certain order. In this case, rotated clockwise 90 degrees."""
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def char_pic_grid(grid):
    # grid[y][x] where i is x and j is y.
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            # Prints each item sequentially without spaces
            print(grid[j][i], end='')
        # Adds newline at end of string.
        print('\n')


def main():
    """Main method to check if char_pic_grid() works properly."""
    char_pic_grid(grid)

# If program is run (and not imported), calls main() method.
if __name__ == '__main__':
    main()
