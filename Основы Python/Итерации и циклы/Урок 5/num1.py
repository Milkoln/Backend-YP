# Пригодится для наполнения списков!
from random import randint as rnd

# 1. Создание списка списков:
rows = 3
harvest = [[rnd(5, 20) for i in range(rows)] for j in range(rows)]

  # Примените list comprehension.

# 2. Функция для подсчёта общего урожая:
def total_harvest(harv : list[list[int]]) -> int:
    return sum(sum(i) for i in harv)

# 3. Функция для подсчёта среднего урожая с каждого участка:
def average_harvest_per_plot(harv : list[list[int]]) -> list[float]:
    return [float(sum(i) / len(i)) for i in harv]

# Вывод результатов
print('Урожай с каждой грядки на каждом участке:', harvest)
print('Общий урожай со всех участков:', total_harvest(harvest))
print('Средний урожай с каждого участка:', average_harvest_per_plot(harvest))