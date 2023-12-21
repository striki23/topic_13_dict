countries: dict = {}
n: int = int(input('Введите кол-во записей: '))

# заносим данные в словарь
for record in range(n):
    data: list = input('Введите страну и города: ').split()
    country: str = data[0]
    cities: list = data[1:]
    if country not in countries.keys():
        countries[country] = cities
    else:
        countries[country] += cities
print('\n')

# ищем город в словаре
m: int = int(input('Введите количество искомых записей: '))
for i in range(m):
    city = input('Введите название города: ').strip().title()

    for k, v in countries.items():
        if city in v:
            print(k)
        else:
            print('город не был найден...')
