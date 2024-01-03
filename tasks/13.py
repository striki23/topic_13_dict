# заносим данные в словарь
election: dict = {}
n: int = int(input('Введите кол-во записей: '))

for record in range(n):
    key, value = input('Введите фамилию кандидата и количество голосов: ').split()
    election[key] = int(election.get(key, 0)) + int(value)
    print(election)
print('\n')

# читаем данные словаря и выводим общее кол-во голосов по каждому кандидату
for candidate, voices in sorted(election.items()):
    print(f'{candidate} | Общее количество голосов: {voices}')
