from Crypto.Util.number import getPrime, bytes_to_long
from random import randint

FLAG = b'CHTB{??????????????????????????????????}'
flag = bytes_to_long(FLAG)

def keygen():
    p, q = getPrime(1024), getPrime(1024)
    N = p*q
    g, r1, r2 = [randint(1,N) for _ in range(3)]
    g1, g2 = pow(g, r1*(p-1), N), pow(g, r2*(q-1), N)
    return [N, g1, g2], [p, q]

def encrypt(m, public):
    N, g1, g2 = public
    assert m < N, "Message is too long"
    s1, s2 = randint(1,N), randint(1,N)
    c1 = m*pow(g1,s1,N) % N
    c2 = m*pow(g2,s2,N) % N
    return [c1, c2]

def decrypt(enc, private):
    c1, c2 = enc
    p, q = private
    m1 = c1 * pow(q, -1, p) * q
    m2 = c2 * pow(p, -1, q) * p
    return (m1 + m2) % (p*q)

public, private = keygen()
enc = encrypt(flag, public)
assert flag == decrypt(enc, private)

print(f'Public key: {public}')
print(f'Encrypted Flag: {enc}')

