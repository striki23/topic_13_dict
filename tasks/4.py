# Программа отображает последовательность кнопок, которую необходимо
# нажать, чтобы на экране телефона появился текст, введенный пользователем.

tabl_t9: dict = {
    1: '.,?!:', 2: 'ABC',
    3: 'DEF', 4: 'GHI',
    5: 'JKL', 6: 'MNO',
    7: 'PQRS', 8: 'TUV',
    9: 'WXYZ', 0: ' '
}
line: str = input().upper()
# --------------
# chars_map: dict = {}
#
# for key, value in tabl_t9.items():
#     for idx, let in enumerate(value, 1):
#         chars_map[let] = str(key) * idx

# --------------

# for symb in line:
#     for k, v in tabl_t9.items():
#         if symb in v:
#             # посчитаем сколько раз нужно выводить цифру
#             count_symb = v.index(symb) + 1
#             print(str(k) * count_symb, end='')

# --------------------------------

chars_map: dict[str, str] = {' ': '0',
                             '!': '1111',
                             ',': '11',
                             '.': '1',
                             ':': '11111',
                             '?': '111',
                             'A': '2',
                             'B': '22',
                             'C': '222',
                             'D': '3',
                             'E': '33',
                             'F': '333',
                             'G': '4',
                             'H': '44',
                             'I': '444',
                             'J': '5',
                             'K': '55',
                             'L': '555',
                             'M': '6',
                             'N': '66',
                             'O': '666',
                             'P': '7',
                             'Q': '77',
                             'R': '777',
                             'S': '7777',
                             'T': '8',
                             'U': '88',
                             'V': '888',
                             'W': '9',
                             'X': '99',
                             'Y': '999',
                             'Z': '9999'}

for char in line:
    print(chars_map.get(char, ''), end='')
