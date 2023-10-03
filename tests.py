import numpy as np


def T(array:list[int])->int:
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

def normalize(array:list[int])->list[float]:
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

def M(array:list[int])->float:
    """
    Функция для подсчета матожидания
    """
    return sum(normalize(array))/(len(array))

def D(array:list[int])->float:
    """
    Функция для подсчета дисперсии
    """
    m = M(array)
    new_array = list((i - m)**2 for i in normalize(array))
    return sum(new_array)/len(array)

def float_equals(a:float,b:float,EPS)->bool:
    """
    Сравнение вещественных чисел с заданной точностью
    """
    return float(a) - float(b) <= EPS

def sequence_bit_test(array:list[int])->float:
    """
    Один из статистических тестов NIST
    Частотный побитовый тест
    Смысл в сравнении количества 1 и 0 в битовом представлении части последовательности
    Идеальное значение - 0.5
    """
    binary_str = ''
    for el in array:
        binary_str += bin(el)
    return binary_str.count('1')/len(binary_str)

def squeeze_test(n_array:list[float])->list[int]:
    """
     Тест на сжатие
     Смысл в умножении числа 2^31 на рандомные числа из последовательности, пока не получим 1
     Считаем количество умножений и рисуем график. В итоге должно получится некое распределение
    """
    TWO_POWER_31 = 2147483648
    res = list()
    for i in range(1000):
        am_of_tries = 0
        tmp = TWO_POWER_31
        while not float_equals(tmp,1,1e-16):
            tmp = tmp * n_array[np.random.randint(1,len(n_array))]
            am_of_tries += 1
        res.append(am_of_tries)
    return res

def is_good_seq(array):
    """
    Проверка последовательности на "хорошесть"
    Если все параметры и тесты в сумме откланяются от идельных не более чем на 20% то
    последовательность хорошая
    """
    if T(array)>=int(len(array)*0.2):
        perf_sum = 1.083
        cur_sum = M(array) + D(array) + sequence_bit_test(array)
        return perf_sum - (perf_sum*0.2) < cur_sum < perf_sum + (perf_sum*0.2)