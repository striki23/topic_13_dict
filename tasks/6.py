# На вход подается строка, где присутствуют дубликаты слов
# Программа добавляет к каждому дубликату слова соотв. постфикс '_n'

line: list = input().split()
new_line: str = ''
for word in line:
    if word not in new_line:
        new_line += word + ' '
    else:
        # заводим счетчик постфикса n
        n = 1
        word_n = f'{word}_{n}'
        while word_n in new_line:
            word_n = f'{word}_{n}'
            n += 1
        new_line += word_n + ' '

print(new_line)
