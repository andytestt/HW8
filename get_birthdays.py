from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())  # Початок поточного тижня (понеділок)
    end_of_week = start_of_week + timedelta(days=6)  # Кінець поточного тижня (неділя)

    birthdays_this_week = []
    for user in users:
        birthday = user['birthday'].date()
        if start_of_week <= birthday <= end_of_week:
            if birthday.weekday() >= 5:  # Якщо день народження - вихідний
                weekday = 'Monday'  # Привітати в понеділок
            else:
                weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                weekday = weekdays[birthday.weekday()]
            birthdays_this_week.append((weekday, user['name']))

    if birthdays_this_week:
        print('Birthdays for this week:')
        for weekday, name in sorted(birthdays_this_week):
            print(f"{weekday}: {name}")
    else:
        print('No birthdays this week')


users = [
    {'name': 'Bill', 'birthday': datetime(2023, 5, 18)},
    {'name': 'Jill', 'birthday': datetime(2023, 5, 20)},
    {'name': 'Kim', 'birthday': datetime(2023, 5, 22)},
    {'name': 'Jan', 'birthday': datetime(2023, 5, 23)}
]

get_birthdays_per_week(users)