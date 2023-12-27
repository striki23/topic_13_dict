# Вводим с новой строки два слова, которые будем проверять
word_1: str = input('Введите первое слово: ').lower()
word_2: str = input('Введите второе слово: ').lower()


# Прописываем функцию, которая создает из строки словарь
# с буквами и их кол-вом
def word_dict(word: str) -> dict[str, int]:
    return {let: word.count(let) for let in word}


# если словарь двух слов равны, то это анаграмм
if word_dict(word_1) == word_dict(word_2):
    print('ДА')
else:
    print('НЕТ')
