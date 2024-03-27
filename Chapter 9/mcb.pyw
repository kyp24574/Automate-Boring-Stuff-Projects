#! python3
"""A program that saves clipboard contents to keywords. Can be listed and deleted."""
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword> - Deletes keyword from shelf.
#        py.exe mcb.pyw delete - Deletes all keywords from shelf.

import pyperclip
import shelve
import sys

# Opens new shelf file and saves it inside a variable
mcb_shelf = shelve.open('mcb')
# Saves clipboard content to keyword.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()

# Deletes clipboard content saved to keyword.
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] in mcb_shelf:
        del mcb_shelf[sys.argv[2]]

# If the length of sys.argv is 2.
elif len(sys.argv) == 2:
    # List keywords in mcb_shelf
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))

    # Deletes all keywords in mcb_shelf
    elif sys.argv[1].lower() == 'delete':
        for key in list(mcb_shelf.keys()):
            del mcb_shelf[key]

    # Loads keyword to clipboard.
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
