from matplotlib import pyplot as plt
from collections import Counter
import numpy as np
import string, hashlib, itertools, random, math

def clean(x):
    return ''.join(c for c in x.upper() if c in string.ascii_letters)

def IoC(x):
    num = sum(x * (x - 1) for _, x in Counter(x).most_common())
    den = len(x) * (len(x) - 1)
    return num / den

def untranspose(c, l):
    n = len(c) // l
    r = []
    s = 0
    for i in range(l):
        t = n
        if len(c) % l > i:
            t = n + 1
        r.append(c[s:s+t])
        s += t
    res = ''.join(''.join(p) for p in itertools.zip_longest(*r, fillvalue=''))
    assert c == ''.join(res[i::l] for i in range(l))
    return res

def quadgramstats(x):
    c = Counter(x[i:i+4] for i in range(len(x) - 4))
    return {k:math.log(v / len(x), 10) for k, v in c.most_common()}

def score(x):
    return sum(targetQuad.get(x[i:i+4], -24) for i in range(len(x) - 4)) / (len(x) - 3)

def fullscore(x, keys):
    return score(untranspose(''.join(x[i::len(keys)].translate(''.maketrans(string.ascii_uppercase, k)) for i, k in enumerate(keys)), len(keys)))

def swap(x, a, b):
    assert a <= b
    if a == b: return x
    return x[:a] + x[b] + x[a+1:b] + x[a] + x[b+1:]

def shuffled(x):
    x = list(x)
    random.shuffle(x)
    return ''.join(x)

def hillclimb(c, K):
    keys = [shuffled(string.ascii_uppercase) for _ in range(K)]
    outer = 0
    best = float("-inf")
    bestk = keys
    while outer < 5000 * K * K // len(c):
        print("iterate")
        for i in range(K):
            keys[i] = shuffled(string.ascii_uppercase)
            target = fullscore(c, keys)
            fails = 0
            while fails < 1000:
                b = random.randrange(1, 26)
                a = random.randrange(1, 26)
                t = keys[:i] + [swap(keys[i], min(a, b), max(a, b))] + keys[i+1:]
                ts = fullscore(c, t)
                if ts > target:
                    target = ts
                    fails = 0
                    keys = t
                else:
                    fails += 1
            if target > best:
                best = target
                bestk = keys
                outer = 0
                print("improved", target)
            else:
                outer += 1
    return bestk

def transform(c, l, k):
    ut = untranspose(c, l)
    return sum(IoC(ut[i::k]) for i in range(k)) / k

reference = clean(open("atotc.txt", "r").read())
targetIoC = IoC(reference)
targetQuad = quadgramstats(reference)
ctxt = clean(open("content.enc.txt", "r").read())

x = np.arange(0.5, 20, 1)
y = np.arange(0.5, 20, 1)
z = np.array([[abs(targetIoC - transform(ctxt, i, j)) for j in range(1, 20)] for i in range(1, 20)])
plt.pcolormesh(x, y, z)
plt.show()

_, K, L = min((z[i - 1][j - 1], j, i) for i in range(1, 20) for j in range(1, 20))
print(f"{K = }")
print(f"{L = }")
ctxt = untranspose(ctxt, L)
with open("qgram.ref", "w") as o:
    o.write(clean(reference))
with open("ctxt.tmp", "w") as o:
    o.write(ctxt)
import os
os.system(f"clang++ -O3 -o hillclimber hillclimber.cpp && ./hillclimber qgram.ref ctxt.tmp {K}")
# keys = hillclimb(ctxt, K)
# print(keys)
# print(untranspose(''.join(ctxt[i::K].translate(''.maketrans(string.ascii_uppercase, keys[i])) for i in range(K)), K))
