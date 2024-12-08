from random import randint as rnd


def get_dumplings_recommendation():
    return rnd(10, 20)

print(f"Оптимальным количеством пельменей на сегодня будет {get_dumplings_recommendation()}")