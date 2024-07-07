
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
 
    today = datetime.today().date()
    upcoming_birthdays = []
    one_week_from_today = today + timedelta(days=7)

    for user in users:
        birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
      
        if today <= birthday_this_year <= one_week_from_today:
            if birthday_this_year.weekday() >= 5:  
                next_monday = birthday_this_year + timedelta(days=(7 - birthday_this_year.weekday()))
                congratulation_date = next_monday
            else:
                congratulation_date = birthday_this_year
            
            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.07.12"},
    {"name": "Jane Smith", "birthday": "1990.07.07"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
