# добавляем новые термины в словарь
slang_d: dict = {}
n = int(input('Введите количество слов для добавления: '))

for i in range(n):
    k, v = input('Введите слово и описание (разделенные двоеточием): ').split(' : ')
    slang_d[k.capitalize()] = v.capitalize()

print('\nПолучить подробное описание сленговых слов')
m = int(input('Введите количество искомых слов: '))
looking_for = [input('Введите слово: ').capitalize() for i in range(m)]

# ищем термины в словаре
for word in looking_for:
    if word not in slang_d:
        print(f'{word} - не найдено ...')
    else:
        print(f'{word} - {slang_d[word]}')
