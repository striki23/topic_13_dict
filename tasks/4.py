# Программа отображает последовательность кнопок, которую необходимо
# нажать, чтобы на экране телефона появился текст, введенный пользователем.

tabl_t9: dict = {1: '.,?!:', 2: 'ABC',
                 3: 'DEF', 4: 'GHI',
                 5: 'JKL', 6: 'MNO',
                 7: 'PQRS', 8: 'TUV',
                 9: 'WXYZ', 0: ' '
                 }
line: str = input().upper()
for symb in line:
    for k, v in tabl_t9.items():
        if symb in v:
            # посчитаем сколько раз нужно выводить цифру
            count_symb = v.index(symb) + 1
            print(str(k)*count_symb, end='')
