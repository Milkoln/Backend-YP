# Вместо многоточия укажите необходимые параметры.
def count_tiles(depth, length, width=None):
    # Опишите условие, когда ширина бассейна не указана.
    if (width is None):
        width = length
    
    # Посчитайте, сколько понадобится плиток для стенок и дна бассейна.
    cnt = 2 * depth * (length + width) + (length * width)

    # Верните результат работы функции.
    return cnt


total_tiles = count_tiles(2, 2, 2)
print('Общее количество плиток для строительства бассейна:', total_tiles)