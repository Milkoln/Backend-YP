# Количество корзин с овощами, шт.
baskets = 462 
# Средний вес овощей в одной корзине, кг.
average_weight = 25
# Стоимость одного килограмма урожая, в монетах.
price_per_kg = 175 


# Допишите функцию, которая рассчитывает вес и стоимость урожая.
def calc(basket_cnt: int, average_weight: int, kg_price: int) -> tuple[int, int]:
    overall_weight = basket_cnt * average_weight
    overall_price = overall_weight * kg_price
    return (overall_weight, overall_price)

# Вызовите функцию calc() и обработайте вернувшееся значение.
weight, price = calc(baskets, average_weight, price_per_kg)
# Составьте f-строку и напечатайте её.
print(f"Общий вес урожая: {weight} кг. Оценённая стоимость урожая: {price}.")