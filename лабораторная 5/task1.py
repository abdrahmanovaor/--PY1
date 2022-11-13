# TODO решить с помощью list comprehension и распечата
from pprint import pprint

dict_translate = [{'bin':bin(i),'dec': (i), 'hex': hex(i), 'oct': oct(i)}for i in range(16)]
pprint(dict_translate)

