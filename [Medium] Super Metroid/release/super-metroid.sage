from Crypto.Util.number import bytes_to_long, getPrime
from secrets import FLAG

def gen_key():
	from secrets import a,b
	E1 = EllipticCurve(F, [a,b])
	assert E.is_isomorphic(E1)
	key = - F(1728) * F(4*a)^3 / F(E1.discriminant())
	return key

def encrypt(message, key):
	m = bytes_to_long(message)
	e = 0x10001
	G = E.lift_x(Integer(m))
	P = e*G
	return int(P[0])^^int(key)

p = getPrime(256)
F = GF(p)
E = EllipticCurve(F, [1,2])
key = gen_key()

c1 = encrypt(FLAG[:22], 0)
c2 = encrypt(FLAG[22:], key)

print(f'p = {p}')
print(f'c1 = {c1}')
print(f'c2 = {c2}')