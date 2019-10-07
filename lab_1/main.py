def calculate_frequences(text: str) -> dict:
    delite = ['.', ',', '-', '_', '', '/', '—', '&', '^', '~', '%', '$', '?', '!', '*', '@', '"', ':', '\n']
    new_txt = {}
    if type(text)!=str:
        return new_txt
    if text is None:
        print('Ошибка')
    filter_txt = ''
    for letter in text:
        if not letter.isdigit() and letter not in delite:
            filter_txt += letter
    filter_txt = filter_txt.split()
    for word in filter_txt:
        word = word.lower()
        if word in new_txt:
            new_txt[word] += 1
        else:
            new_txt[word] = 1
    return new_txt

    print(calculate_frequences(text))


def filter_stop_words(frequencies: dict, stop_words: tuple):
    my_dict = {}
    if stop_words is None or frequencies is None or len(frequencies) == 0:
        print('Ошибка')
        return {}
    if type(frequencies) is not dict:
        return {}
    for key, value in frequencies.items():  # возвращает список пар кортежей
        if key not in stop_words and isinstance(key, str):  # проверка принадлежности к str
            my_dict[key] = value
    return my_dict

def get_top_n(my_dict: dict, top_n: int):
    list_freq=[]
    if my_dict is None or top_n<=0:
        return()
    else:
        list_freq=sorted(my_dict, key=my_dict.get, reverse=True)  # get возвращает значение для данного ключа,reverse-опциональный параметр
    return tuple(list_freq[:top_n])
    print(get_top_n(my_dict, top_n))
