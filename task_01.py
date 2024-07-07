from datetime import datetime

def get_days_from_today(date):
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        result = (today - date_obj).days
        return result
    except:
        raise ValueError("Дата в неправильному форматі!")
    
print(get_days_from_today("2024-05-09"))