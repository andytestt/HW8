from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())  # Початок поточного тижня (понеділок)
    end_of_week = start_of_week + timedelta(days=6)  # Кінець поточного тижня (неділя)

    birthdays_this_week = []
    next_week = False

    for user in users:
        birthday = user['birthday'].date()
        birthday_this_year = datetime(datetime.now().year, birthday.month, birthday.day).date()

        if (start_of_week <= birthday_this_year <= end_of_week) or (end_of_week.year < start_of_week.year and (start_of_week <= birthday_this_year or birthday_this_year <= end_of_week)):
            if birthday_this_year.weekday() >= 5:  # Якщо день народження - вихідний
                weekday = 'Monday'  # Привітати в понеділок
            else:
                weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                weekday = weekdays[birthday_this_year.weekday()]
            birthdays_this_week.append((weekday, user['name']))
        elif birthday_this_year > end_of_week and not next_week:
            next_week = True

    if birthdays_this_week:
        print('Birthdays for this week:')
        for weekday, name in sorted(birthdays_this_week):
            print(f"{weekday}: {name}")
    elif next_week:
        print('No birthdays this week, but there are birthdays next week.')
    else:
        print('No birthdays this week.')

users = [
    {'name': 'Bill', 'birthday': datetime(1012, 6, 8)},
    {'name': 'Jill', 'birthday': datetime(2013, 6, 10)},
    {'name': 'Kim', 'birthday': datetime(2001, 6, 13)},
    {'name': 'Jan', 'birthday': datetime(2010, 6, 4)}
]

get_birthdays_per_week(users)