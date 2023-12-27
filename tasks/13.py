# заносим данные в словарь
election: dict = {}
n: int = int(input('Введите кол-во записей: '))

for record in range(n):
    key, value = input('Введите фамилию кандидата и количество голосов: ').split()
    value = int(value)
    if key not in election:
        election[key] = (value,)
    else:
        election[key] += (value,)
print('\n')

# читаем данные словаря и выводим общее кол-во голосов по каждому кандидату
for candidate, voices in sorted(election.items()):
    print(f'{candidate} | Общее количество голосов: {sum(voices)}')
