# Объявите функцию get_stickers_comparison() с параметрами collection_1 и collection_2.
# Эта функция должна возвращать кортеж из трёх коллекций:
# - уникальные_стикеры из collection_1,
# - уникальные_стикеры из collection_2,
# - стикеры, которые есть в collection_1 и в collection_2.

def get_stickers_comparison(collection_1 : list[str], collection_2 : list[str]):
    collection_1_s = set(collection_1)
    collection_2_s = set(collection_2)
    only_first = sorted(collection_1_s.difference(collection_2_s))
    only_second = sorted(collection_2_s.difference(collection_1_s))
    common = sorted(collection_1_s.intersection(collection_2_s))
    return tuple([only_first, only_second, common])


# Списки стикеров:
stas_collection = ['Тим Бернерс-Ли', 'Линус Торвальдс', 'Ада Лавлейс', 'Линус Торвальдс', 'Маргарет Гамильтон', 'Бьярн Страуструп']
anton_collection = ['Тим Бернерс-Ли', 'Гвидо ван Россум', 'Линус Торвальдс', 'Бьярн Страуструп', 'Бьярн Страуструп', 'Кен Томпсон', 'Деннис Ричи']

# Вызываем функцию и распаковываем полученный кортеж в три переменные:
stas_stickers, anton_stickers, common_stickers = get_stickers_comparison(stas_collection, anton_collection)
# Печатаем результаты:
print('Стикеры, которые есть только у Стаса:', stas_stickers)
print('Стикеры, которые есть только у Антона:', anton_stickers)
print('Стикеры, которые есть и у Стаса, и у Антона:', common_stickers)