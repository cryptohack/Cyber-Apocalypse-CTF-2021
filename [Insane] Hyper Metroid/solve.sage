def data_to_jacobian(data):
	xs, ys = data
	pt_x = R(list(map(FF, xs)))
	pt_y = R(list(map(FF, ys)))
	pt = (pt_x, pt_y)
	return J(pt)

def alien_prime(a):
	p = (a^5 - 1) // (a - 1)
	assert is_prime(p)
	return p

def find_order(a,i,j):
	g = 2
	n = 5
	p = (a^n - 1) // (a - 1)

	k = CyclotomicField(n)
	zeta = k.gen()

	r = a % 5
	if r == 0:
		zetak = -zeta
	elif r == 2:
		zetak = -zeta^4
	elif r == 3:
		zetak = zeta^2
	elif r == 4:
		zetak = zeta^3

	J = zetak * prod([ (k(a) - zeta^(1/l) ) for l in range(1,g+1)])
	N = norm(J + (-1)^i * zeta^j)
	return N

a = 1152921504606846997
p = alien_prime(a)
alpha = 1532495540865888942099710761600010701873734514703868973

FF = FiniteField(p)
R.<x> = PolynomialRing(FF)

h = 1
f = alpha*x^5

C = HyperellipticCurve(f,h,'u,v')
J = C.jacobian()
J = J(J.base_ring())

enc_flag = ([1276176453394706789434191960452761709509855370032312388696448886635083641, 989985690717445420998028698274140944147124715646744049560278470410306181, 1], [617662980003970124116899302233508481684830798429115930236899695789143420, 429111447857534151381555500502858912072308212835753316491912322925110307])

JQ = data_to_jacobian(enc_flag)
order = find_order(a, 0, 1)
e = 2873198723981729878912739
d = inverse_mod(e, order)

rec_JP = d*JQ
rec_x = rec_JP[0].roots()[0][0]
print(int(rec_x).to_bytes(28, 'big'))
