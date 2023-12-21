# Программа считает кол-во очков на основании введенной строки.
# Стоимость каждой буквы отражена в доп таблице

tabl_scores: dict = {1: ('A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'),
                2: ('D', 'G'),
                3: ('B', 'C', 'M', 'P'),
                4: ('F', 'H', 'V', 'W', 'Y'),
                5: ('K',),
                8: ('J', 'X'),
                10: ('Q', 'Z')
                }
line: str = input('Введите ваш текст: ')
scores: int = 0
for symb in line.upper():
    for k, v in tabl_scores.items():
        if symb in v:
            scores += k
print(f'{line} оценивается в {scores} очков!')
