from Crypto.Util.number import getPrime, inverse
import random

def main():
    print("They want my private key, but it has sentimental value to me. Please help me and send them something different.")
    p = getPrime(512)
    q = getPrime(512)
    N = p*q
    phi = (p - 1) * (q - 1)
    e = 0x10001
    d = inverse(e, phi)
    print({'e': e, 'd': d, 'N': N})
    d2 = int(input("> "))
    assert d2 != d
    assert 0 <= d2 < phi
    with open("flag.txt") as f:
        flag = f.read()
    random.seed(str(d2) + flag)
    for _ in range(50):
        m = random.randrange(N)
        c = pow(m, e, N)
        assert m == pow(c, d2, N)
    print(flag)

if __name__ == "__main__":
    import os
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    main()
