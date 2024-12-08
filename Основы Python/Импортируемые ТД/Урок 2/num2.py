# Допишите нужные импорты.
import datetime as dt

def timedelta_days(datetime_str_1, datetime_str_2):
    datetime1 = dt.datetime.strptime(datetime_str_1, '%Y/%m/%d %H:%M:%S')
    datetime2 = dt.datetime.strptime(datetime_str_2, '%Y/%m/%d %H:%M:%S')
    delta = datetime2 - datetime1
    return delta.days

difference = timedelta_days('2019/05/10 00:00:00', '2019/10/04 00:00:00')

print('От начала посевной до начала сбора урожая прошло', difference, 'дней.')