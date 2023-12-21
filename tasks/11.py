# добавляем контакты в телефонную книжку
phone_nums: dict = {}
n: int = int(input('Введите кол-во записей: '))

for record in range(n):
    k, v = input('Введите имя и телефон: ').split()
    if k not in phone_nums.keys():
        phone_nums[k] = (v,)
    else:
        phone_nums[k] += (v,)

# ищем абонента в словаре
m: int = int(input('Введите количество искомых абонентов: '))
for i in range(m):
    name: str = input('Введите имя абонента: ')
    if name not in phone_nums:
        print('абонент не найден...')
    else:
        print(*phone_nums[name])
