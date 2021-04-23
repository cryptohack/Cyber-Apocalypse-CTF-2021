import random

FLAG = b"CHTB{Imai_and_Matsumoto_play_with_multivariate_cryptography}"
q = 2^8
n = 60

X = GF(2)['Y'].gen()
F.<alpha> = GF(q, name='ɑ', modulus=X^8 + X^4 + X^3 + X^2 + 1)
_F = PolynomialRing(F, [f'x{i}' for i in range(n)])
dummies = _F.gens()
PR.<X> = F['X']
poly = PR.irreducible_element(n)
assert poly.is_irreducible()
K = PR.quotient_ring(poly.subs({poly.variables()[0]: X}), names=["X"])
_K = _F['Z'].quotient_ring(K.modulus())
X = K.gen()

beta = vector(K, [X^i for i in range(n)])

def xlist(x):
    return (x.list() + [0 for _ in range(n)])[:n]

def phi_inv(x):
    return sum(b*y for b, y in zip(beta, x))

def phi(x):
    # https://ask.sagemath.org/question/52594/how-to-get-the-coefficient-of-a-multivariate-polynomial-with-respect-to-a-specific-variable-and-degree-in-a-quotient-ring/
    # Note, this *really* only works for this particular \beta
    return vector(F, xlist(x))

def keygen():
    _beta = vector(_K, [_K.gen()^i for i in range(n)])
    # Repeated for use with a lifted beta
    def phi_inv(x):
        return sum(b*y for b, y in zip(_beta, x))
    def phi(x):
        # https://ask.sagemath.org/question/52594/how-to-get-the-coefficient-of-a-multivariate-polynomial-with-respect-to-a-specific-variable-and-degree-in-a-quotient-ring/
        # Note, this *really* only works for this particular \beta
        return vector(_F, xlist(x))

    def reduce(f):
        for d in dummies:
            f %= (d^q + d)
        return f

    def matgen():
        while True:
            A = random_matrix(F,n,n)
            if A.is_invertible():
                return A
            
    while True:
        theta = random.randrange(1, n)
        h = q^theta + 1
        if gcd(h, q^n - 1) == 1:
            break
    h_inv = inverse_mod(h, q^n - 1)
    
    A = matgen()
    c = vector(F, [alpha^random.randrange(q) for _ in range(n)])
    L1 = lambda x: A * x + c
    L1_inv = lambda x: A^-1 * (x - c)
    _L1 = lambda x: A.change_ring(_F) * x + c.change_ring(_F)
    
    B = matgen()
    d = vector(F, [alpha^random.randrange(q) for _ in range(n)])
    L2 = lambda x: B * x + d
    L2_inv = lambda x: B^-1 * (x - d)
    _L2 = lambda x: B.change_ring(_F) * x + d.change_ring(_F)

    frob = []
    for beta_i in beta:
        frob.append(xlist((beta_i^q)))
    frob = Matrix(F, frob).T^theta
    def psi(x):
        a = phi_inv(frob.change_ring(_F) * x)
        b = phi_inv(x)
        c = a * b
        return phi(c)
    
    x_bar = vector(_F, dummies)
    u_bar = _L1(x_bar)
    v_bar = psi(u_bar)
    y_bar = _L2(v_bar)

    yb2 = []
    for f in y_bar:
        for dummy in dummies:
            f %= dummy^q + dummy
        yb2.append(f)
    y_bar = vector(_F, yb2)
    
    return (y_bar, ((A, c), (B, d), h_inv))

def encrypt(pub, mes):
    assert len(pub) == len(mes)
    d = {x: m for x, m in zip(dummies, mes)}
    return vector(F, [f.substitute(d) for f in pub])

def decrypt(priv, ct):
    (A, c), (B, d), h_inv = priv
    L1_inv = lambda x: A^-1 * (x - c)
    L2_inv = lambda x: B^-1 * (x - d)
    return L1_inv(phi(phi_inv(L2_inv(ct))^h_inv))
