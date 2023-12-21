line: list = input().lower().split()

d: list = []
for idx, word in enumerate(line):
    d.append(line[:idx].count(word))
print(*d)

# не поняла как тут использовать словарь, т.к. ни слова,
# ни кол-во повторений не является уникальным значением,
# т.о. не могут быть использованы в качестве ключа