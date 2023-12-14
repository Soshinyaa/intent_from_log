import random

def generate_typos(word, num_typos):
    """
    Функция генерирует массив с ошибками и опечатками для данного слова
    num_typos - количество ошибок и опечаток
    Возвращает словарь, ключом которого является изначальная версия слова,
    а значением массив с модифицированными словами
    """
    if len(word) < 3:
        return 
    
    typo_chars = 'абвгдежзийклмнопрстуфхцчшщэюя'  # Допустимые символы для замены, нет ь, ы, ъ, ё
    typos = []
    dict_generate = {}
    for _ in range(num_typos):
        modified_word = word
        index = random.randint(0, len(word) - 1)  # Случайный индекс для замены символа
        typo_char = random.choice(typo_chars)  # Случайный символ замены
        modified_word = modified_word[:index] + typo_char + modified_word[index + 1:]
        typos.append(modified_word)
    

    # Сгенерировать слова более короткой длины
    for index in range(len(word) - 1):
        modified_word = word[:index + 1]
        if len(modified_word) > 2:
            typos.append(modified_word)

    # Сгенерировать слова более длинной длины
    for _ in range(num_typos):
        modified_word = word
        index = random.randint(0, len(word) - 1)  # Случайный индекс для добавления символа
        typo_char = random.choice(typo_chars)  # Случайный символ для добавления
        modified_word = modified_word[:index + 1] + typo_char + modified_word[index + 1:]
        typos.append(modified_word)
    dict_generate[word] = typos

    for _ in range(num_typos):
        modified_word = word
        index = random.randint(0, len(word) - 1)  # Случайный индекс для добавления символа
        modified_word = modified_word[:index + 1] + ' ' + modified_word[index + 1:]
        typos.append(modified_word)
    dict_generate[word] = typos

    for _ in range(num_typos):
        modified_word = word
        index = random.randint(0, len(word) - 1)  # Случайный индекс для удаления символа
        modified_word = modified_word[:index] + modified_word[index+1:]
        if random.choice([True, False]):
            index = random.randint(0, len(modified_word) - 1)  # Второй случайный индекс, если нужно удалить еще один символ
            modified_word = modified_word[:index] + modified_word[index+1:]
        typos.append(modified_word)
    dict_generate[word] = typos
    
    return dict_generate

word = "резьба"
generate_typos(word, 100)
