import zlib
from math import log

def shannon (data):
    if data == None or data == '':
    	data = ' '
    data = list(bytearray(data))
    dataSize = len(data)
    ent = 0.0
    for i in range(256):
        freq = float(data.count(i))/dataSize
        if freq > 0:
            ent = ent + freq * log(freq, 2)
    return -ent

def kolmogorov(data):
   if data == None or data == '':
   	return 0.0
   l = float(len(data))
   compr = zlib.compress(data)
   c = float(len(compr))/l
   if c > 1:
     return 1.0
   else:
     return c
