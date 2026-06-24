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
    def generate_month(year, month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_names = ["January", "February", "March", "April", "May", "June", 
                   "July", "August", "September", "October", "November", "December"]
    
    if month == 2 and is_leap_year(year):
        days_in_month[1] = 29
        
    start_day = get_start_day(year, month)
    
    calendar_output = f"\n  {month_names[month-1]} {year}\n"
    calendar_output += "Su Mo Tu We Th Fr Sa\n"
    
    # Fill initial spaces
    calendar_output += "   " * start_day
    
    for day in range(1, days_in_month[month-1] + 1):
        calendar_output += f"{day:2} "
        start_day += 1
        if start_day == 7:
            calendar_output += "\n"
            start_day = 0
            
    return calendar_output + "\n"
def generate_400_years(start_year):
    with open("400_year_calendar.txt", "w") as file:
        for year in range(start_year, start_year + 400):
            file.write(f"=== YEAR {year} ===\n")
            for month in range(1, 13):
                file.write(generate_month(year, month))
            file.write("\n")
    print(f"Calendar from {start_year} to {start_year + 399} generated successfully.")

if __name__ == "__main__":
    # Generate 400 years starting from 2000
    generate_400_years(2000)

