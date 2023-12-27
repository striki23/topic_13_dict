# На вход подается строка, где присутствуют дубликаты слов
# Программа добавляет к каждому дубликату слова соотв. постфикс '_n'

line: list = input().split()

# new_line: str = ''
# for word in line:
#     if word not in new_line:
#         new_line += word + ' '
#     else:
#         # заводим счетчик постфикса n
#         n = 1
#         word_n = f'{word}_{n}'
#         while word_n in new_line:
#             word_n = f'{word}_{n}'
#             n += 1
#         new_line += word_n + ' '

# print(new_line)

# -----------------------------

words_count, result = {}, []

for word in line:
    if word not in result:
        result.append(word)
    else:
        # if word in words_count:
        #     words_count[word] += 1
        # else:
        #     words_count[word] = 1

        words_count[word] = words_count.get(word, 0) + 1

        print(words_count)
        template = f'{word}_{words_count.get(word)}'
        result.append(template)
print(*result)

# TODO: Разобраться с задачей
