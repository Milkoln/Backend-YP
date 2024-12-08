class Employee:
    vacation_days = 28
    first_name, second_name, gender = str(), str(), str()
    def __init__(self, _first_name, _second_name, _gender):
        self.first_name = _first_name
        self.second_name = _second_name
        self.gender = _gender

# Создайте экземпляры класса Employee с различными значениями атрибутов.
employee1 = Employee('Walter', 'White', 'м')
employee2 = Employee('Egor', 'Krid', 'м')

# Допишите код для вывода информации о сотрудниках.
print(f'Имя: {employee1.first_name}, Фамилия: {employee1.second_name}, Пол: {employee1.gender}, Отпускных дней в году: {employee1.vacation_days}.')
print(f'Имя: {employee2.first_name}, Фамилия: {employee2.second_name}, Пол: {employee2.gender}, Отпускных дней в году: {employee2.vacation_days}.')