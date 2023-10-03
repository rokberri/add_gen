import generator
from tests import *

gen = generator.Generator(32568449)

array = gen.generate_list(2500)
print(squeeze_test(normalize(array)))
generate_visual_output(array)

