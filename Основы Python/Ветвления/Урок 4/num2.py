# Код этой функции не меняйте.
def count_tiles(depth, length, width=None):
    if width is None:
        width = length

    width_side = 2 * width * depth
    length_side = 2 * length * depth
    bottom_tiles = length * width
    total = width_side + length_side + bottom_tiles

    return total

# Передайте в функцию нужный параметр и напишите её код.
def make_phrase(cnt):
    #str_init = "Для строительства бассейна нужно заготовить 125 плиток"
    str_plit = ''
    if (11 <= cnt <= 14):
        str_plit = f"{cnt} плиток"
    elif (cnt % 10 == 1):
        str_plit = f"{cnt} плитку"
    elif (2 <= cnt % 10 <= 4):
        str_plit = f"{cnt} плитки"
    else:
        str_plit = f"{cnt} плиток"
    return str_plit


total_tiles = count_tiles(2, 2, 2)
# Выведите на экран нужное сообщение.
print("Для строительства бассейна нужно заготовить " + make_phrase(total_tiles))