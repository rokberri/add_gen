import generator
from tests import *
from visual_outputs import generate_visual_output


# В идеале генерировать много последовательностей, меняя изначально заданную и коэфицент m
# Нужно это чтоб понять, правда ли генератор выдает неплохие последовательности
# Тут в цикле я меняю только m, посмотри файл с генератором, чтоб понять что как 

TEST_VALUE = 32568449
for i in range(5000):
    gen = generator.Generator(i) 
    array = gen.generate_list(2500)
    if is_good_seq(array):
        generate_visual_output(array, i)
