sequence_1 = [69, 59, 57, 60, 63, 44, 46, 69]
sequence_2 = [33, 73, 50, 25, 36, 68, 52, 76]

def compare_sequences(arr1, arr2) -> str:
    if (arr1 > arr2):
        return f"Список {arr1} больше."
    if (arr1 == arr2):
        return "Списки равны."
    return f"Список {arr2} больше."

# Вызовите функцию compare_sequences(),
# передайте в неё списки sequence_1 и sequence_2.
# Напечатайте результат, который вернёт функция.
res = compare_sequences(sequence_1, sequence_2)
print(res)