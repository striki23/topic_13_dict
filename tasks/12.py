line: list = input().lower().split()

d: list = []
for idx, word in enumerate(line):
    d.append(line[:idx].count(word))
print(*d)

# Option №2
words_count: dict[str, int] = {}
for word in line:
    words_count[word] = words_count.get(word, 0) + 1
    print(words_count.get(word) - 1, end=' ')
