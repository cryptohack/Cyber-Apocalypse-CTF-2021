from random import randint
from math import gcd
from Crypto.Util.number import long_to_bytes, bytes_to_long

p = 2**1024 + 1657867
MASK = (2**p.bit_length() - 1)
g = 3

def forgery(y: int):
	e = randint(1, p-1)
	r = y*pow(g,e,p) % p
	s = -r % (p - 1)
	m = (e*s) % (p-1)
	m += (bytes_to_long(b'get_flag') << 1200)
	M = hex(m)[2:]
	return(M,r,s)

y = int(input('public key: '))
M, r, s = forgery(y)
print(f'M: {M}')
print(f'r: {r}')
print(f's: {s}')
