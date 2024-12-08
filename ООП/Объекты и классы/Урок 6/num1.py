class BacteriaProducer:
    capacity = 0
    # Допишите инициализатор класса 
    def __init__(self, max_bacteria):
        self.capacity = max_bacteria
        self.size = 0

    # Допишите метод
    def create_new(self):
        if (self.capacity == self.size):
            print('Нет места под новую бактерию')
            return
        self.size += 1
        print('Добавлена одна бактерия. Количество бактерий в популяции:', self.size)

    # Допишите метод
    def remove_one(self):
        if (self.size == 0):
            print('В популяции нет бактерий, удалять нечего')
            return
        self.size -= 1
        print('Одна бактерия удалена. Количество бактерий в популяции:', self.size)


# Пример запуска для самопроверки
bacteria_producer = BacteriaProducer(max_bacteria=3)
bacteria_producer.remove_one()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.remove_one()