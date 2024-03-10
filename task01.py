from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    today = datetime.today().date()
    birthdays = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            day_of_week = birthday_this_year.weekday()

            if day_of_week == 5 or day_of_week == 6:
                birthday_this_year = birthday_this_year + timedelta(days=(7 - day_of_week))

            day_of_week = birthday_this_year.strftime('%A')
            birthdays[day_of_week].append(name)

    for day_of_week, names in birthdays.items():
        print(f'{day_of_week}: {", ".join(names)}')

users = [
    {"name": "Angel Phillips", "birthday": datetime(1985,3,20)},
    {"name": "Anthony Robinson", "birthday": datetime(1985,3,9)},
    {"name": "Melissa Miller", "birthday": datetime(1985,3,10)},
    {"name": "Sheila Hall", "birthday": datetime(1985,3,11)},
    {"name": "Jordan Sanchez", "birthday": datetime(1985,3,12)},
    {"name": "Micheal Villa", "birthday": datetime(1985,3,16)},
]

get_birthdays_per_week(users)
