# заносим данные в словарь
election: dict = {}
n: int = int(input('Введите кол-во записей: '))

for record in range(n):
    k, v = input('Введите фамилию кандидата и количество голосов: ').split()
    if k not in election.keys():
        election[k] = (v,)
    else:
        election[k] += (v,)
print('\n')

# читаем данные словаря и выводим общее кол-во голосов по каждому кандидату
for candidate, voices in sorted(election.items()):
    print(f'{candidate} | Общее количество голосов: {sum(map(int, voices))}')
