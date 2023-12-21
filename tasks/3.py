# Программа считает кол-во очков на основании введенной строки.
# Стоимость каждой буквы отражена в доп таблице
from pprint import pprint

# tabl_scores: dict = {1: ('A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'),
#                      2: ('D', 'G'),
#                      3: ('B', 'C', 'M', 'P'),
#                      4: ('F', 'H', 'V', 'W', 'Y'),
#                      5: ('K',),
#                      8: ('J', 'X'),
#                      10: ('Q', 'Z')
#                      }
# line: str = input('Введите ваш текст: ')
# scores: int = 0
# for symb in line.upper():
#     for k, v in tabl_scores.items():
#         if symb in v:
#             scores += k
# print(f'{line} оценивается в {scores} очков!')

# points: dict[str, int] = {}
# for point, letters in tabl_scores.items():
#     points |= {}.fromkeys(letters, point)
# points.update({}.fromkeys(letters, point))
#
# pprint(points)


tabl_scores: dict[str, int] = {
    'A': 1,
    'B': 3,
    'C': 3,
    'D': 2,
    'E': 1,
    'F': 4,
    'G': 2,
    'H': 4,
    'I': 1,
    'J': 8,
    'K': 5,
    'L': 1,
    'M': 3,
    'N': 1,
    'O': 1,
    'P': 3,
    'Q': 10,
    'R': 1,
    'S': 1,
    'T': 1,
    'U': 1,
    'V': 4,
    'W': 4,
    'X': 8,
    'Y': 4,
    'Z': 10
}

line: str = input('Введите ваш текст: ').upper()
print(f'{line} оценивается в '
      f'{sum(tabl_scores.get(i) for i in line if i in tabl_scores)} очков!')
