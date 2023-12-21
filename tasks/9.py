# Вводим с новой строки два слова, которые будем проверять
line_1: str = \
    ''.join(input('Введите первое слово: ').lower().split()).replace(',', '')
line_2: str = \
    ''.join(input('Введите первое слово: ').lower().split()).replace(',', '')


# Прописываем функцию, которая создает из строки словарь
# с буквами и их кол-вом
def word_dict(word):
    d:dict = {i: word.count(i) for i in word}
    return d


# если словарь двух строк равны, то это анаграмм
if word_dict(line_1) == word_dict(line_2):
    print('ДА')
else:
    print('НЕТ')
