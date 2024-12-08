# Напишите функцию get_competition_data().
def get_competition_data(races_info : list[dict[str, int]]):
    participants = set()
    winner : tuple[str, int]
    partic_with_overall_score : dict[str, int] = dict()
    for race in races_info:
        for ks, val in race.items():
            if (ks in partic_with_overall_score):
                partic_with_overall_score[ks] += val
            else:
                partic_with_overall_score[ks] = val
            participants.add(ks)
    
    max_val = 0
    for dude, dude_score in partic_with_overall_score.items():
        if dude_score > max_val:
            winner = dude, dude_score,
            max_val = dude_score
    participantsl = sorted(list(participants))
    parts_str = ', '.join(participantsl)
    print('Команды, участвовавшие в гонке: ' + parts_str)
    print(f'В гонке победила команда {winner[0]} с результатом {winner[1]} баллов')


races_data = [
    {'Ferrari': 20, 'Mercedes': 5, 'Aston Martin': 10, 'Williams': 15},
    {'Mercedes': 15, 'Aston Martin': 20, 'Ferrari': 10, 'Williams': 0},
    {'Ferrari': 20, 'Williams': 15, 'Aston Martin': 10, 'Mercedes': 5}
]


get_competition_data(races_data)