def print_valid_cities(all_cities, used_cities):
    not_used = all_cities.difference(used_cities)
    for city in not_used:
        print(city)
    # Вместо этого многоточия напишите код функции, она должна
    # принимать и обрабатывать аргументы all_cities и used_cities,
    # а затем печатать результат в нужном формате

all_cities = {
    'Абакан',
    'Астрахань', 
    'Бобруйск', 
    'Калуга',
    'Караганда',
    'Кострома',
    'Липецк', 
    'Новосибирск'
}

used_cities = {'Калуга', 'Абакан' , 'Новосибирск'}

print_valid_cities(all_cities, used_cities)