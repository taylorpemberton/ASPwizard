from bs4 import BeautifulSoup

html_code = """
<table class="tg"><tbody><tr><th class="header"><strong>Date</strong></th><th class="header"><strong>Holiday</strong></th></tr><tr><td class="cell1">Jan 1, Mon</td><td class="cell1">New Year's Day*</td></tr><tr><td class="cell2">Jan 6, Sat</td><td class="cell2">Three Kings' Day</td></tr><tr><td class="cell1">Jan 15, Mon</td><td class="cell1">Martin Luther King, Jr. Day</td></tr><tr><td class="cell2">Feb 9-Feb 10, Fri-Sat</td><td class="cell2">Lunar New Year's Eve &amp; Lunar New Year</td></tr><tr><td class="cell1">Feb 12, Mon</td><td class="cell1">Lincoln's Birthday</td></tr><tr><td class="cell2">Feb 14, Wed</td><td class="cell2">Ash Wednesday</td></tr><tr><td class="cell1">Feb 19, Mon</td><td class="cell1">Washington's Birthday (Presidents' Day)</td></tr><tr><td class="cell2">Mar 24, Sun</td><td class="cell2">Purim</td></tr><tr><td class="cell1">Mar 28, Thurs</td><td class="cell1">Holy Thursday</td></tr><tr><td class="cell2">Mar 29, Fri</td><td class="cell2">Good Friday</td></tr><tr><td class="cell1">Apr 10-Apr 11, Wed-Thurs</td><td class="cell1">Idul-Fitr (Eid al-Fitr)</td></tr><tr><td class="cell2">Apr 23-Apr 24, Tue-Wed</td><td class="cell2">Passover</td></tr><tr><td class="cell1">Apr 29-Apr 30, Mon-Tue</td><td class="cell1">Passover (7th and 8th Days)</td></tr><tr><td class="cell2">May 2, Thurs</td><td class="cell2">Holy Thursday (Orthodox)</td></tr><tr><td class="cell1">May 3, Fri</td><td class="cell1">Good Friday (Orthodox)</td></tr><tr><td class="cell2">May 9, Thurs</td><td class="cell2">Solemnity of the Ascension</td></tr><tr><td class="cell1">May 27, Mon</td><td class="cell1">Memorial Day*</td></tr><tr><td class="cell2">June 12-June 13, Wed-Thurs</td><td class="cell2">Shavuot (2 Days)</td></tr><tr><td class="cell1">June 17-June 18, Mon-Tue</td><td class="cell1">Idul-Adha (Eid al-Adha)</td></tr><tr><td class="cell2">June 19, Wed</td><td class="cell2">Juneteenth</td></tr><tr><td class="cell1">July 4, Thurs</td><td class="cell1">Independence Day*</td></tr><tr><td class="cell2">Aug 13, Tue</td><td class="cell2">Tisha B'Av</td></tr><tr><td class="cell1">Aug 15, Thurs</td><td class="cell1">Feast of the Assumption</td></tr><tr><td class="cell2">Sept 2, Mon</td><td class="cell2">Labor Day*</td></tr><tr><td class="cell1">Oct 3-Oct 4, Thurs-Fri</td><td class="cell1">Rosh Hashanah</td></tr><tr><td class="cell2">Oct 12, Sat</td><td class="cell2">Yom Kippur</td></tr><tr><td class="cell1">Oct 14, Mon</td><td class="cell1">Italian Heritage Day/Indigenous Peoples' Day</td></tr><tr><td class="cell2">Oct 17-Oct 18, Thurs-Fri</td><td class="cell2">Succoth (2 Days)</td></tr><tr><td class="cell1">Oct 24, Thurs</td><td class="cell1">Shemini Atzereth</td></tr><tr><td class="cell2">Oct 25, Fri</td><td class="cell2">Simchas Torah</td></tr><tr><td class="cell1">Nov 1, Fri</td><td class="cell1">Diwali</td></tr><tr><td class="cell2">Nov 1, Fri</td><td class="cell2">All Saints' Day</td></tr><tr><td class="cell1">Nov 5, Tues</td><td class="cell1">Election Day</td></tr><tr><td class="cell2">Nov 11, Mon</td><td class="cell2">Veterans Day</td></tr><tr><td class="cell1">Nov 28, Thurs</td><td class="cell1">Thanksgiving Day*</td></tr><tr><td class="cell2">Dec 9, Mon</td><td class="cell2">Immaculate Conception</td></tr><tr><td class="cell1">Dec 25, Wed</td><td class="cell1">Christmas Day*</td></tr></tbody></table>
"""

# Parse the HTML
soup = BeautifulSoup(html_code, 'html.parser')

# Find the table containing holiday information
holiday_table = soup.find('table', class_='tg')

# Extract holiday information from the table
holidays = []
if holiday_table:
    for row in holiday_table.find_all('tr')[1:]:  # Skip the header row
        columns = row.find_all('td')
        date = columns[0].text.strip()
        holiday = columns[1].text.strip()
        holidays.append((date, holiday))

# Write the extracted holiday information to a file
with open("holidays_2024.txt", "w") as file:
    for date, holiday in holidays:
        file.write(f"Date: {date}, Holiday: {holiday}\n")
