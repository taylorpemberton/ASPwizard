from icalendar import Calendar, Event
from datetime import datetime, timedelta

# Open the file for reading
with open('holidays_2024.txt', 'r') as file:
    for line in file:
        # Split the line by commas and extract date and holiday
        parts = line.strip().split(', ')
        date_info = parts[0].split(': ')[1]  # Extract date information
        holiday = parts[2].split(': ')[1]  # Extract holiday information

        # Check if the date information contains a day of the week
        if ',' in date_info:
            # Extract day of the week, month, and day
            day_of_week, month, day = date_info.split(', ')[1].split(' ')
        else:
            # Extract month and day
            month, day = date_info.split(' ')

        # Convert month abbreviation to a number
        month_number = {
            'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
            'May': 5, 'June': 6, 'July': 7, 'Aug': 8,
            'Sept': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
        }[month]

        # Convert to datetime object
        date = datetime(2024, month_number, int(day))

        # Print or process the date and holiday as needed
        print("Date:", date.strftime("%b %d, %a"), "Holiday:", holiday)
