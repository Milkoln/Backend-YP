def print_pack_report(starting_value):
    for i in range(starting_value, 0, -1):
        iss = str(i)
        if (i % 15 == 0):
            print(iss + " - расфасуем по 3 или по 5")
        elif (i % 5 == 0):
            print(iss + ' - расфасуем по 5')
        elif (i % 3 == 0):
            print(iss + ' - расфасуем по 3')
        else:
            print(iss + ' - не заказываем!')

print_pack_report(31)