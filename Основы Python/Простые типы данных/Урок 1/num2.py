# Получаем данные в секундах
response = 424562

# Переведите полученное значение в необходимые единицы измерения
days = response // (3600 * 24)
hours = (response % (3600 * 24)) // 3600
minutes = ((response % (3600 * 24)) % 3600) // 60
seconds = (((response % (3600 * 24)) % 3600) % 60)

print(response, 'секунд - это')
print('Дней:', days)
print('Часов:', hours)
print('Минут:', minutes)
print('Секунд:', seconds)