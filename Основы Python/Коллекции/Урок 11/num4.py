def pay_bills(month, bills):
    if (month % 3 == 0):
        return bills[1:len(bills)-1]
    return [bills[0], bills[-1]]


# Вызов функции:
print(pay_bills(5, ['Интернет', 'Коммуналка', 'Телефон', 'Страховка']))