from random import randint

# Начальная температура чая
current_temperature = 85

while (current_temperature > 60):
    delta_temp = randint(1, 3)
    current_temperature -= delta_temp
    print("Прошла минута.")
    print(f"Чай остыл ещё на {delta_temp} °C. Текущая температура: {current_temperature} °C ")
print('Время пить чай!')