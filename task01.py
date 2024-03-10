"""
Завдання 1
На першому етапі вам потрібно реалізувати функцію для виведення списку колег, яких потрібно привітати з днем народження 
на тижні.
У вас є список словників users, кожен словник у ньому обов'язково має ключі name та birthday. Така структура 
представляє модель списку користувачів з їх іменами та днями народження. Де name — це рядок з ім'ям користувача,
а birthday — це datetime об'єкт, в якому записаний день народження.
"""
#  from faker import Faker
#  fake = Faker(locale="uk_UA")
# # Кількість записів
# num_records = 10

# # Створення списку 
# list_of_dicts = []

# for _ in range(num_records):
#     birthday = fake.date_of_birth(minimum_age=18, maximum_age=90)
#     birthday = birthday.replace(month=3)
#     person_dict = {
#         "name": fake.name(),
#         "birthday": fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%d.%m.%Y"),
##         "birthday": birthday.strftime("%d.%m.%Y"),
#         "phone": fake.phone_number()
#     }
#     list_of_dicts.append(person_dict)

# print(list_of_dicts)


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
