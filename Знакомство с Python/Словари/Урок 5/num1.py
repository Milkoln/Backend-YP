friends_names = ['Аня', 'Коля', 'Лёша', 'Лена', 'Миша']
friends_cities = ['Владивосток', 'Красноярск', 'Москва', 'Обнинск', 'Чебоксары']

# Объявлен пустой словарь, его нужно будет наполнить элементами, 
# каждый из которых составлен по схеме "имя: город"
friends =  {}

# Допишите ваш код сюда
for i in range(len(friends_names)):
    friends[friends_names[i]] = friends_cities[i]

print(f"Лена живёт в городе {friends['Лена']}")