from datetime import datetime, timedelta

users = [
    {"name": "Angel Phillips", "birthday": "01.04.1985"},
    {"name": "Anthony Robinson", "birthday": "14.03.1985"},
    {"name": "Melissa Miller", "birthday": "11.03.1985"},
    {"name": "Sheila Hall", "birthday": "25.03.1985"},
    {"name": "Jordan Sanchez", "birthday": "10.03.1985"},
    {"name": "Micheal Villa", "birthday": "16.03.1985"},
]

def get_birthdays_this_week(users):
    today = datetime.today()
    start_week = today - timedelta(days=today.weekday())
    end_week = start_week + timedelta(days=7)
    
    birthdays_this_week = []
    
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%d.%m.%Y")
        if start_week <= birthday.replace(year=today.year) < end_week:
            birthdays_this_week.append(user["name"])
    
    return birthdays_this_week    

print (get_birthdays_this_week(users))
