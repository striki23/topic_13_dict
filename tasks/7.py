# добавляем новые термины в словарь
slang_d: dict = {}

for i in range(int(input('Введите количество слов для добавления: '))):

    key, value = input('Введите слово и описание (разделенные двоеточием): ').split(' : ')
    slang_d[key.capitalize()] = value.capitalize()

print('\nПолучить подробное описание сленговых слов')
m = int(input('Введите количество искомых слов: '))
looking_for = [input('Введите слово: ').capitalize() for i in range(m)]

# ищем термины в словаре
for word in looking_for:
    print(f'{word} - {slang_d.get(word, "не найдено ...")}')
