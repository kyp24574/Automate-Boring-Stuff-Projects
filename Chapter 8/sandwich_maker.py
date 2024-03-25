# sandwich_maker.py - A program that simulates building a sandwich. Uses pyinputplus for user input.

import pyinputplus as pyip

def sandwich_maker():
    """Simulates the sandwich making process."""
    print('What are your sandwich preferences? Please go through the menu options below.')
    # Base cost of sandwich
    cost = 5.00
    # Asks user for bread type
    bread = pyip.inputMenu(['Wheat', 'White', 'Sourdough'], 'Bread Type:\n')
    if bread.lower() == 'sourdough':
        # If user chooses sourdough, add 0.20 to cost
        cost += 0.20
    # Asks user for protein type
    protein = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], 'Protein Type:\n')
    if protein.lower() == 'chicken':
        # If user chooses chicken, add 0.15 to cost
        cost += 0.15
    # Asks user if they want cheese; if yes, what kind
    cheese = pyip.inputYesNo('Cheese?\n')
    if cheese.lower() == 'yes':
        cheese = pyip.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'], 'What kind?\n')
        # Add 0.50 to cost if yes
        cost += 0.10
    # Asks user if they want basic toppings
    toppings = pyip.inputYesNo('Would you like mayo, mustard, lettuce, and/or tomato?\n')
    if toppings.lower() == 'yes':
        # Adds 0.50 to cost if yes
        cost += 0.50
    # Asks how many the user wants
    quantity = pyip.inputInt('How many sandwiches would you like?\n')
    # Multiplies cost and quantity for total cost.
    cost *= quantity
    print('Your total cost is $%.2f.' % cost)


def main():
    """Main method to check if sandwich_maker() method works."""
    sandwich_maker()

# If program is run (and not imported), calls main() method.
if __name__ == '__main__':
    main()
