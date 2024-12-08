# Пропишите нужные импорты.
import datetime as dt

weekdays_ru = ['понедельник', 'вторник', 'среда', 
               'четверг', 'пятница', 'суббота', 'воскресенье']

def get_weekday_name(weekday_number: int):
    return weekdays_ru[weekday_number]


def get_day_after_tomorrow(date_string):
    # Напишите код функции.
    date_formated = dt.datetime.strptime(date_string, '%Y-%m-%d')


    day_today = get_weekday_name(date_formated.weekday())
    delta_time = dt.timedelta(days=2)
    date_after_two_days = date_formated + delta_time
    day_after_tom = get_weekday_name(date_after_two_days.weekday())
    print(f"Сегодня {date_string}, {day_today}, а послезавтра будет {day_after_tom}")


# Проверьте работу программы, можете подставить свои значения.
get_day_after_tomorrow('2024-01-01')
get_day_after_tomorrow('2024-01-02')
get_day_after_tomorrow('2024-01-03')
get_day_after_tomorrow('2024-01-04')
get_day_after_tomorrow('2024-01-05')
get_day_after_tomorrow('2024-01-06')