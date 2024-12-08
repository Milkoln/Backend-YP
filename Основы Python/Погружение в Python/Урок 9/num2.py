c_sharp = 375
java = 546
javascript = 915
php = 288
python = 603
langs = [c_sharp, java, javascript, php, python]

def analyze_jobs():
    # Вычислите общее количество исследованных вакансий.
    total_jobs = sum(langs)
    # Вычислите процент вакансий для Python от общего числа вакансий
    # и округлите результат до двух знаков (до сотых долей):
    python_percent = round(python * 100 / total_jobs, 2)
    # Напечатайте фразы, описанные в задании (две строки).
    print(f"Общее число исследованных вакансий, в тысячах: {total_jobs}")
    print(f"Вакансии для Python-разработчиков, в %: {python_percent}")

analyze_jobs()