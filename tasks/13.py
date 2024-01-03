# заносим данные в словарь
election: dict[str, int] = {}

for record in range(int(input('Введите кол-во записей: '))):
    key, value = input('Введите фамилию кандидата и количество голосов: ').split()
    election[key] = election.get(key, 0) + int(value)
print('\n')

# читаем данные словаря и выводим общее кол-во голосов по каждому кандидату
for candidate, voices in sorted(election.items()):
    print(f'{candidate} | Общее количество голосов: {voices}')
