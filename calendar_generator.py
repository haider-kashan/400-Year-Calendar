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
def get_start_day(year, month):
    """Calculates the day of the week the month starts on."""
    # Standard formula to find the starting day of any given month/year
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    day = (1 + ((13 * (month + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)) % 7
    # Adjusting so 0 = Sunday, 1 = Monday, etc.
    return (day + 5) % 7