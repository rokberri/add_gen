import matplotlib.pyplot as plt
from tests import *


def generate_visual_output(array:list[int], i:int)->None:
    """
    Генерация сводного графика со всеми необходимыми данными 
    Период, матожидание, дисперсия, визуальный тест, распределения сквиз теста
    Значения числа m
    """
    n_array = normalize(array)
    fig = plt.figure()
    fig.set_size_inches(15,10)
    fig.suptitle(f"""
                m: {i}
                T: {T(array)}
                M: {M(array)}
                D: {D(array)}
                Sequence bit result: {sequence_bit_test(array)}
                """)
    spreading(fig, n_array)
    visual_test(fig, n_array)
    squeeze_test_output(fig, n_array)
    fig.savefig(f"fig/{i}_data.png")

def squeeze_test_output(fig:plt.Figure,n_array:list[float])->None:
    """
    Генерация гистограммы для сквиз теста
    """
    ax = fig.add_subplot(133)
    ax.hist(squeeze_test(n_array))

def visual_test(fig:plt.Figure,n_array:list[float])->None:
    """
    Визуальный тест на случайность распределения чисел
    Каждый пиксель в квадрате 50х50 закрашивается в зависимости от числа(цвет поменять можно) )
    """
    ax = fig.add_subplot(132)
    ax = ax.imshow(np.array(n_array).reshape(50,50))

def spreading(fig:plt.Figure,n_array:list[float])->None:
    """
    Отображение распределения чисел на гистограмме
    """
    ax = fig.add_subplot(131)
    ax.hist(n_array,100)