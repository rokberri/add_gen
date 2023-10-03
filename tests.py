import matplotlib.pyplot as plt
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

def D(array:list[int], M:float)->float:
    """
    Функция для подсчета дисперсии
    """
    new_array = list((i - M)**2 for i in normalize(array))
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

def spreading(fig:plt.Figure,n_array:list[float])->None:
    """
    Отображение распределения чисел на гистограмме
    """
    ax = fig.add_subplot(131)
    ax.hist(n_array,100)

def squeeze_test_output(fig:plt.Figure,n_array:list[float])->None:
    ax = fig.add_subplot(133)
    ax.hist(squeeze_test(n_array))

def visual_test(fig:plt.Figure,n_array:list[float])->None:
    """
    Визуальный тест на случайность распределения чисел
    Каждый пиксель в квадрате 50х50 закрашивается в зависимости от числа(цвет поменять можно) )
    """
    ax = fig.add_subplot(132)
    ax = ax.imshow(np.array(n_array).reshape(50,50))

def generate_visual_output(array:list[int])->None:
    """
    Генерация сводного графика со всеми необходимыми данными 
    Период, матожидание, дисперсия, визуальный тест, распределения сквиз теста
    Значения числа m
    """
    fig = plt.figure()
    fig.set_size_inches(15,10)
    n_array = normalize(array)
    spreading(fig, n_array)
    visual_test(fig, n_array)
    squeeze_test_output(fig, n_array)
    fig.savefig(f"hist.png")
