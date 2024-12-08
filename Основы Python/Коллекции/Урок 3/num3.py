def assess_yield(number_of_plants, average_weight) -> tuple[float, str]:
    overall_weight : float = float(number_of_plants * average_weight / 1000)
    message_str : str = ''
    if (overall_weight > 100):
        message_str = 'Ожидается отличный урожай.'
    elif (overall_weight > 50):
        message_str = 'Ожидается хороший урожай.'
    elif (overall_weight > 0):
        message_str = 'Урожай будет так себе.'
    else:
        message_str = 'Урожая не будет.'
    result : tuple[float, str] = overall_weight, message_str,
    return result

# Пример вызова функции
total_weight, rating = assess_yield(50, 200)
print(total_weight, 'кг.', rating)