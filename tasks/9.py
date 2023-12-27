# Вводим с новой строки два слова, которые будем проверять
line_1: str = ''.join(input('Введите первое слово: ').lower().split())
line_2: str = ''.join(input('Введите первое слово: ').lower().split())


# Прописываем функцию, которая создает из строки словарь
# с буквами и их кол-вом
def word_dict(word: str) -> dict[str, int]:
    return {let: word.count(let) for let in word if let.isalnum()}


# если словарь двух строк равны, то это анаграмм
if word_dict(line_1) == word_dict(line_2):
    print('ДА')
else:
    print('НЕТ')
