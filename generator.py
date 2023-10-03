
DEFAULT_STRING = "7618 983 4434 3758 1544 1685 2639 4102 6898 9313 253 2162 1841 9726 5732 5265 751 6961 5088 5765 2090 3086 9334 867 4259 8426 4768 8526 732 2229 9756 6900 2726 8572 292 3805 2322 2032 2395 8837 408 3460 4115 3369 447 3239 5392 2044 296 5122 5881 3667 6219 3386 9480 7362 3119 8988 9020 1728 5684 9932 1066 7475 6890"
class Generator:
    """
    Класс генератора ПСЧП.
    При инициализации задается начальный ряд чисел размерностью 65 для генерации последующих чисел
    и число m(от него будет зависеть максимальный период ряда)
    """
    def __init__(self, m):
        self.base_num_row = [int(el) for el in DEFAULT_STRING.split(' ')]# можно генерировать разными методами, я просто с рандоморга взял числа)
        self.m = m # определяет максимально возможный период последовательности 
        
    def generate_list(self, n):
        """
        Метод для генерации последовательности
        В целом аддитивный генератор работает как числа Фибоначи, просто изначально заданных значений побольше
        """
        if n < 65:
            return self.base_num_row[::n] # в случае если юзер дебил и просит нас последовательность меньше, чем изначальная
        else:
            row = list(self.base_num_row) # если таки юзер умный, присваиваем последовательности изначальные значени
            for ind in range(65,n,1):
                row.append((row[ind-18] + row[ind-65]) % self.m) # и добавляем новые пока по формуле, пока не дополним до нужного количества
        return row
