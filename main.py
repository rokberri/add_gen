import matplotlib as plt
import generator
from tests import *

gen = generator.Generator(32568449)

array = gen.generate_list(10000)
print(D(array,0.48))

