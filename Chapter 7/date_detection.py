# date_detection.py - A program to detect dates in the DD/MM/YYYY format.
import re

def date_detection(text):
    """Detects dates in the DD/MM/YYYY."""
    # Regular expression for date detection in different formats
    # dd/mm/yyyy
    # dd.mm.yyyy
    # dd-mm-yyyy
    date_regex = re.compile(r'''(
        (\d?\d)                 # Day
        (\.|-|/)                # Separator 
        (0?\d|1[0-2])           # Month
        (\.|-|/)                # Separator
        ([12]\d{3})             # Year
        )''', re.VERBOSE)

    # list to store valid dates
    valid_dates = []
    # Loops through list of matches found
    for date in date_regex.findall(text):
        # Manually adds leading zero if there is no leading zero
        if len(date[1]) == 1:  # checks date length
            date_list = list(date)  # Tuple to List
            date_list[1] = '0'+date_list[1]  # adds zero to date
            if len(date[3]) == 1:  # checks month length
                date_list[3] = '0'+date_list[3]  # Adds zero to month
            date_list[0] = ''.join(date_list[1:])  # creates new date
            date = tuple(date_list)  # List to Tuple

        # Converts day, month, and year to int values
        day = int(date[1])
        month = int(date[3])
        year = int(date[5])

        # If day is greater than 31, passes
        if day > 31:
            continue
        # Checks for leap year
        if month == 2:
            if day <= 28:
                valid_dates.append(date[0])  # Adds to valid date
            else:
                leap = False
                if (year % 4 == 0) and (year % 100 != 0):
                    leap = True
                elif (year % 400 == 0) and (year % 100 == 0):
                    leap = True
                if day == 29 and leap:
                    valid_dates.append(date[0])  # Adds to valid date if leap year.
        # Checks months with 30 days
        elif month in [4, 6, 9, 11] and day <= 30:
            valid_dates.append(date[0])
        # Adds date to list otherwise.
        else:
            valid_dates.append(date[0])

    # Prints valid dates if found.
    if not valid_dates:
        print('No valid dates found.')
    else:
        print(valid_dates)


def main():
    """Main method to check date_detection() method."""
    # Test string; can be edited.
    text = '2/12/2015'
    date_detection(text)

# If program is run (and not imported), calls main() method.
if __name__ == '__main__':
    main()
