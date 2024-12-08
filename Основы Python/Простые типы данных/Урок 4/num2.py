def find_answer():
    number = 3
    # Далее проводите операции над number отдельно по шагам
    number = number * 100
    number = number / 5
    number = number - 20
    number = number + 2
    # Верните результат:
    return int(number)


# Вызовите функцию find_answer() и напечатайте результат.
print("Ответ на главный вопрос жизни, Вселенной и всего такого: " + str(find_answer()))