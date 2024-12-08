# Напишите функцию get_competition_data().
def get_competition_data(races_info : list[dict[str, int]]):
    participants = set()
    for race in races_info:
        ks = race.keys()
        participants.update(set(ks))
    participantsl = sorted(list(participants))
    parts_str = ', '.join(participantsl)
    print('Команды, участвовавшие в гонке: ' + parts_str)


races_data = [
    {'Ferrari': 20, 'Mercedes': 5, 'Aston Martin': 10, 'Williams': 15},
    {'Mercedes': 15, 'Aston Martin': 20, 'Ferrari': 10, 'Williams': 0},
    {'Ferrari': 20, 'Williams': 15, 'Aston Martin': 10, 'Mercedes': 5}
]


get_competition_data(races_data)