# Пользователь вводит текст. На основе этого текста создается словарь.
# Ключами словаря служат символы из текста, а значениями кол-во символов.

line: list = [i.upper() for i in input('Введите ваш текст: ')]
chars_count = {}
for char in line:
    if char not in chars_count:
        chars_count[char] = line.count(char)
print(chars_count)
