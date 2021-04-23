# https://eprint.iacr.org/2004/241.pdf, section 4.3.1
# Koblitz, Algebraic Aspects of Cryptography, chapter 6

enc = ([1276176453394706789434191960452761709509855370032312388696448886635083641, 989985690717445420998028698274140944147124715646744049560278470410306181, 1], [617662980003970124116899302233508481684830798429115930236899695789143420, 429111447857534151381555500502858912072308212835753316491912322925110307])

from Crypto.Util.number import long_to_bytes

def alien_prime(a):
    p = (a^5 - 1) // (a - 1)
    assert is_prime(p)
    return p


_e = 2873198723981729878912739
def encrypt(Px):
    e = _e
    P = C.lift_x(Px)
    JP = J(P)
    print(JP)
    return e * JP

def compute_order():
    n = 5
    g = (n - 1) // 2
    z = CyclotomicField(n).gen()
    sigma_inv = lambda i, z: z^(1/i)
    Jsum = {0: -z, 2: -z^4, 3: z^2, 4: z^3}[a % 5] * prod(a - sigma_inv(i, z) for i in range(1, g + 1))
    return norm(Jsum + z) # z because we're working over a twist

def decrypt(P):
    d = inverse_mod(_e, compute_order())
    return FF(-(d * P)[0][0])

def transmit_point(P):
    mumford_x = P[0].list()
    mumford_y = P[1].list()
    return (mumford_x, mumford_y)

def untransmit(x):
    return J([R(x[0]), R(x[1])])


a = 1152921504606846997
alpha = 1532495540865888942099710761600010701873734514703868973
p = alien_prime(a)
assert (a^5 - 1) % (a - 1) == 0
assert p % 5 == 1
assert pow(alpha, (p - 1)//5, p) == a

FF = FiniteField(p)
R.<x> = PolynomialRing(FF)

h = 1
f = alpha*x^5

# v^2 + v = alpha * u^5
C = HyperellipticCurve(f,h,['u','v'])
print(C)
J = C.jacobian()
J = J(J.base_ring())
print(long_to_bytes(decrypt(untransmit(enc))))
