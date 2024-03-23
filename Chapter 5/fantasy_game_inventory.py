# fantasy_game_inventory.py - A program to display any passed "inventory".
"""A program designed to display a player's inventory in a formatted way."""

def display_inventory(inventory):
    """Displays inventory to screen."""
    print('Inventory:')
    # Total number of items stored.
    total_items = 0
    # Loops through inventory.
    for key, value in inventory.items():
        # Prints quantity then name.
        print(str(value) + ' ' + key)
        total_items += value  # adds to total
    print('Total number of items: %s' % total_items)  # prints total amount


def add_to_inventory(inventory, added_items):
    """Adds loot to inventory."""
    # Loops through list of loot
    for loot in added_items:
        # If loot does not exist in inventory, defaults to 0.
        inventory.setdefault(loot, 0)
        inventory[loot] += 1
    # Returns updated inventory.
    return inventory


def main():
    """Main method to test display_inventory() and added_to_inventory()."""
    inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    display_inventory(inventory)
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inventory = add_to_inventory(inventory, dragon_loot)
    display_inventory(inventory)


if __name__ == '__main__':
    main()
