# Пропишите нужные импорты.
import datetime as dt

# Напишите код функции, следуя плану из задания.
def get_results(leader_time, participant_time):
    if (leader_time == participant_time):
        print(f"Вы пробежали за {leader_time} и победили!")
        return
    leader_time_dt = dt.datetime.strptime(leader_time, "%H:%M:%S")
    participant_time_dt = dt.datetime.strptime(participant_time, "%H:%M:%S")
    delta_time = participant_time_dt - leader_time_dt
    print(f"Вы пробежали за {participant_time} с отставанием от лидера {delta_time}")


# Проверьте работу программы, можете подставить свои значения.
get_results('02:02:02', '02:02:02')
get_results('02:02:02', '03:04:05')