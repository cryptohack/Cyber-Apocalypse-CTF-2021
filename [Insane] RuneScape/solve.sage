with open("output.txt", "r") as f:
    out = f.read().strip().splitlines()

def ev(vvv):
    return eval(vvv.replace("^", "**"))

x = GF(2)['x'].gen()
F.<alpha> = GF(2^8, name="alpha", modulus=ev(out[1].split(" by ")[1]))
PF.<X> = F['X']
poly = ev(out[3].split("with modulus ")[1])
n = poly.degree()
K.<X> = PF.quotient_ring(poly)

M1 = Matrix(F, ev(out[66].split("M1: ")[1]))
k1 = vector(F, ev(out[67].split("k1: ")[1]))
M2 = Matrix(F, ev(out[69].split("M2: ")[1]))
k2 = vector(F, ev(out[70].split("k2: ")[1]))

L1 = lambda x: M1 * x + k1
L1inv = lambda x: M1^-1 * (x - k1)
L2 = lambda x: M2 * x + k2
L2inv = lambda x: M2^-1 * (x - k2)

flag1 = vector(F, ev(out[-2].split("encryption: ")[1]))
flag2 = vector(F, ev(out[-1].split("decryption: ")[1]))

def xor(a, b):
    return bytes(x ^^ y for x, y in zip(a, b))

def F_to_byte(f):
    return f.integer_representation()

def V_to_bytes(v):
    return bytes(map(F_to_byte, v))

beta = [X^i for i in range(n)]

def xlist(x):
    return (x.list() + [0 for _ in range(n)])[:n]

def phi_inv(x):
    return sum(b*y for b, y in zip(beta, x))

def phi(x):
    return vector(F, xlist(x))

psi = lambda u: u^h
psi_inv = lambda u: u^h_inv

def encrypt(x):
    return L2(phi(psi(phi_inv(L1(x)))))

def decrypt(y):
    return L1inv(phi(psi_inv(phi_inv(L2inv(y)))))

q = 2^8
for theta in range(n):
    h = q^theta + 1
    if gcd(h, q^n - 1) != 1:
        continue
    h_inv = inverse_mod(h, q^n - 1)
    print(f"Try {theta = }")
    a = decrypt(flag1)
    b = encrypt(flag2)
    print(xor(V_to_bytes(a), V_to_bytes(b)))
