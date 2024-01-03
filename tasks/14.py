countries: dict = {}

# заносим данные в словарь
for record in range(int(input('Введите кол-во записей: '))):
    data: list = input('Введите страну и города: ').split()
    key, *values = data
    countries[key] = countries.get(key, set()) | set(values)
print(countries)
print('\n')

# ищем город в словаре
for look_record in range(int(input('Введите количество искомых записей: '))):
    city = input('Введите название города: ').strip().title()

    for country, cities in countries.items():
        if city in cities:
            print(country)
        else:
            print('город не был найден...')
