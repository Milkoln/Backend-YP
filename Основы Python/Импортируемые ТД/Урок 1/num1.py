# Из модуля decimal импортируйте тип данных Decimal и параметр getcontext.
# Из модуля math импортируйте константу "пи".
from decimal import Decimal, getcontext
from math import pi

# Приведите константу "пи" к типу Decimal.
# Помните, что Decimal() принимает строку, а константа "пи" - это число.
p = Decimal(str(pi))
# Установите необходимую точность для вычислений.
getcontext().prec = 10

# Объявите функцию find_ellipse_area() с двумя параметрами.
find_ellipse_area = lambda a, b : a * b * p

# Объявите три переменные типа Decimal -
# две длины полуосей эллипса и глубину пруда.
a = Decimal('2.5')
b = Decimal('1.75')
c = Decimal('0.35')

# Вызовите функцию find_ellipse_area(), в аргументах передайте длины полуосей эллипса.
area = find_ellipse_area(a, b)

# Вычислите объём пруда: площадь * глубина.
volume = area * c

# Напечатайте фразы с результатами вычислений.
print(f"Площадь эллипса: {area} кв.м.\nОбъём воды для наполнения пруда: {volume} куб.м.")