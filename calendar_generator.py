# calendar_generator.py
def is_leap_year(year):
    """Returns True if the year is a leap year, False otherwise."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False
