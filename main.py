from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    today = datetime.now()
    # print("Today:", today)

    birthdays_per_week = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
        'Saturday': [],
        'Sunday': []
    }

    for user in users:
        name = user['name']
        birthday = user['birthday']
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days < 7:
            greeting_day = (today + timedelta(days=delta_days)).strftime('%A')
            # print(name, ":", birthday_this_year, "->", greeting_day)
            birthdays_per_week[greeting_day].append(name)
    for day, l in birthdays_per_week.items():
        if len(l) > 0:
            converted_list_of_users = ', '.join(l)
            print('{:>4}: {:^10}'.format(day, converted_list_of_users))


data = [
    {'name': 'Bill Gates', 'birthday': datetime(1955, 3, 6)},
    {'name': 'Bill Gates', 'birthday': datetime(1955, 3, 5)},
    {'name': 'Bill Gates', 'birthday': datetime(1955, 3, 4)},
    {'name': 'Jill Valentine', 'birthday': datetime(1981, 3, 3)},
    {'name': 'Kim Kardashian', 'birthday': datetime(1980, 3, 2)},
    {'name': 'Jan Koum', 'birthday': datetime(1976, 2, 28)},
    {'name': 'Jin Koum', 'birthday': datetime(1976, 2, 28)}
]

get_birthdays_per_week(data)
