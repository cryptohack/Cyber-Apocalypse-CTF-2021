from random import randint
from math import gcd
from Crypto.Util.number import long_to_bytes, bytes_to_long

def gen_keys():
    x = randint(1, p-2)
    y = pow(g, x, p)
    return (x, y)

def sign(message: str, x: int):
    while True:
        m = int(message, 16) & MASK
        k = randint(2, p-2)
        if gcd(k, p - 1) != 1:
            continue 
        r = pow(g, k, p)
        s = (m - x*r) * pow(k,-1,p-1) % (p - 1)
        if s == 0:
            continue
        return (r,s)

def verify(message: str, r: int, s: int, y: int):
    m = int(message, 16) & MASK
    if any([x <= 0 or x >= p-1 for x in [m,r,s]]):
        return False
    return pow(g, m, p) == (pow(y, r, p) * pow(r, s, p)) % p

def get_flag(message: str, r: int, s: int, y: int):
    if b'get_flag' not in bytes.fromhex(message):
        return 'Error: message does not request the flag'
    elif verify(message, r, s, y):
        return FLAG
    else:
        return 'Error: message does not match given signature'

if __name__ == "__main__":
    import os
    os.chdir(os.path.abspath(os.path.dirname(__file__)))

    with open("flag.txt", 'rb') as f:
        FLAG = f.read()

    p = 2**1024 + 1657867
    g = 3
    MASK = (2**p.bit_length() - 1)

    x, y = gen_keys()
    print(f"Server's public key: {y}")
    
    print(f'Please send your request message and signature (r,s)')

    message = input('message: ')
    r = int(input('r: '))
    s = int(input('s: '))

    flag = get_flag(message, r, s, y)
    print(flag)