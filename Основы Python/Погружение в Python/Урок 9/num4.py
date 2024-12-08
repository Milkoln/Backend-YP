from random import randint as rnd


def get_dumplings_recommendation(a, b):
    return rnd(a, b)

print(f"Оптимальным количеством пельменей на сегодня будет {get_dumplings_recommendation(25, 30)}")