# Пропишите нужные импорты.
from decimal import Decimal, getcontext


def get_monthly_payment(credit_sum : int, months_cnt : int, bank_percent : int):
    # Банк делит названную сумму на названное количество месяцев 
    # и увеличивает ежемесячный платёж на оговоренный процент.
    getcontext().prec = 3
    credit_sum_d = Decimal(str(credit_sum))
    months_cnt_d = Decimal(str(months_cnt))
    bank_percent_d = Decimal(str(bank_percent))
    monthly_sum = (credit_sum_d / months_cnt_d) * (1 + (bank_percent_d / 100))
    return Decimal(str(monthly_sum))


# Вызовите функцию get_monthly_payment() 
# с указанными в задании аргументами
# и распечатайте нужное сообщение.
sport_payment = get_monthly_payment(54, 24, 9)
print(f"Ежемесячный платёж: {sport_payment} ВтК")