# The flag consists of only uppercase ascii letters
# You do have to fix up the flag format yourself

import string, hashlib, itertools

def clean(x):
    return ''.join(c for c in x.upper() if c in string.ascii_letters)

def transpose(x, l):
    return ''.join(x[i::l] for i in range(l))

def alphabet(r):
    a = list(string.ascii_uppercase)
    for i in range(len(a) - 1, 0, -1):
        j = r.randrange(0, i)
        a[i], a[j] = a[j], a[i]
    return ''.join(a)

def encrypt(text, l, key):
    enc = text.translate(''.maketrans(string.ascii_uppercase, key))
    return transpose(enc, l)

class RNG:
    A = 101565695086122187
    C = 56502943171806276
    M = 288230376151711717
    def __init__(self, seed):
        self.state = seed

    def next(self):
        self.state = ((self.state * self.A) + self.C) % self.M
        return self.state

    def randrange(self, low, high):
        assert high > low
        range = high - low
        limit = range * (self.M // range)
        while True:
            res = self.next()
            if res <= limit:
                return (res % range) + low

if __name__ == "__main__":
    with open("content.txt", "r") as f:
        text = clean(f.read())
    with open("flag.txt", "r") as f:
        text += clean(f.read())
    seed = int.from_bytes(hashlib.sha256(text.encode()).digest(), "big")
    rng = RNG(seed)
    L = rng.randrange(1, 100)
    print(f"{L = }")
    key = alphabet(rng)
    with open("content.enc.txt", "w") as f:
        f.write(encrypt(text, L, key))
