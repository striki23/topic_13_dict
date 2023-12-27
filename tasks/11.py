# добавляем контакты в телефонную книжку
phone_nums: dict = {}

for record in range(int(input('Введите кол-во записей: '))):
    key, value = input('Введите имя и телефон: ').split()
    key = key.capitalize()
    phone_nums[key] = phone_nums.get(key, []) + [value]

# ищем абонента в словаре
for i in range(int(input('Введите количество искомых абонентов: '))):
    name: str = input('Введите имя абонента: ').capitalize()
    print(*phone_nums.get(name, ['абонент не найден...']))
