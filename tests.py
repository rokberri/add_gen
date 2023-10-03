def T(array):
    """
    Находим период последовательности
    Сработает только для большого количества элементов(но их и так много надо)
    Если длина последовательности меньше изначально заданной
    Возвращаем ошибку(нет смысла, ды и не найдем мы период)
    Если больше, то отсекаем изначальные значения и из оставшихся делаем множество
    """
    if len(array)<65:
        print("Too small to find T")
        exit()
    return len(set(array[65::]))

def normalize(array):
    """
    Минимально-максимальная нормализация
    Метод для номализации значений
    (приведения всех значений к единому диапазону, в данном случае [0..1))
    Нужно чтоб корректно посчитать матожидание М и дисперсию D
    """
    max_el = max(array)
    min_el = min(array)
    normalize_data = list()
    for el in array:
        try:
            normalize_data.append((el - min_el)/(max_el - min_el)) # формула для нормализации
        except ZeroDivisionError:
            normalize_data.append(1 * len(normalize_data)) # поднимаю ошибку чисто на всякий случай, на практике нужно очень постараться чтоб её поймать
    return normalize_data

def M(array):
    """
    Функция для подсчета матожидания
    """
    return sum(normalize(array))/(len(array))

def D(array, M):
    """
    Функция для подсчета дисперсии
    """
    new_array = list((i - M)**2 for i in normalize(array))
    return sum(new_array)/len(array)