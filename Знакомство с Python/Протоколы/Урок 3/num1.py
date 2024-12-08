user_query = 'как стать бэкенд-разработчиком'
words = user_query.split()

url = 'https://yandex.ru/search/?text=' +  "%20".join(words)

print(url)