import ast
import string
from pymorphy2 import MorphAnalyzer
morph = MorphAnalyzer()

#Считаем уникальные слова и выводим количество их повторений
def count_unique_words(array):    
    # Создаем словарь для хранения количества повторений каждого слова
    word_counts = {}
    top_dict = {}
    # Подсчитываем количество повторений каждого слова
    for word in array:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    # Сортируем слова по количеству повторений в обратном порядке
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Собираем результат в словарь top_dict, оставляем только слова длиной больше 1
    for word, count in sorted_words:
        if len(word) > 1:
            top_dict[f"{word}"] = f"{count}"
    return top_dict


def start():
    # Открываем полученные данные, преобразуем их в словарь python
    with open('dict.txt', 'r') as file:
        data = file.read()
        data = data.replace('"Value"','').replace('"Key"','').replace('{:','{').replace(',:',':')
        data = data.replace('{','').replace('}','').replace("[","{").replace("]","}")

    data = ast.literal_eval(data)

    #Добавляем все значения в строку,используя ее, проводится весь дальнейший анализ
    stroka = ''
    
    for key, value in data.items():
        stroka += value + ' '

    #Избавляемся от всей пунктуации     
    stroka = stroka.translate(str.maketrans('', '', string.punctuation)).lower()

    #Массив, который будет содержать обработанные слова (в начальной форме)
    parsed = []

    #создаем массив
    stroka = stroka.split()

    #лемматизируем каждое слово в массиве
    for word in stroka:
        word = morph.parse(word)[0]
        word = word.normal_form
        parsed.append(word)

    return count_unique_words(parsed)


