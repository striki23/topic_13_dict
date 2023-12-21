# добавляем новые термины в словарь
synonyms_d: dict = {}
n: int = int(input('Введите количество слов для добавления: '))

for i in range(n):
    k, v = input('Введите слово и синоним: ').split()
    synonyms_d[k.capitalize()] = v.capitalize()

looking_for: str = input('Введите искомое слово: ').capitalize()

# ищем синоним в словаре (в ключах и значениях)
for k, v in synonyms_d.items():
    if looking_for == k:
        print(v)
    if looking_for == v:
        print(k)
