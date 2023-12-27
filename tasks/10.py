# добавляем новые термины в словарь
synonyms_d: dict = {}
n: int = int(input('Введите количество слов для добавления: '))

for i in range(n):
    key, value = input('Введите слово и синоним: ').split()
    synonyms_d[key.capitalize()] = value.capitalize()

looking_for: str = input('Введите искомое слово: ').capitalize()

# ищем синоним в словаре (в ключах и значениях)
for key, value in synonyms_d.items():
    if looking_for == key:
        print(value)
    if looking_for == value:
        print(key)
