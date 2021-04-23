from collections import Counter
import string, itertools, math

def clean(x):
    return ''.join(c for c in x.upper() if c in string.ascii_letters)

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

def fullscore(x, key):
    return score(x.translate(''.maketrans(string.ascii_uppercase, key)))

def swap(x, a, b):
    assert a <= b
    if a == b: return x
    return x[:a] + x[b] + x[a+1:b] + x[a] + x[b+1:]

def hillclimb(c):
    key = string.ascii_uppercase
    target = fullscore(c, key)
    change = True
    while change:
        change = False
        for a in range(1, 26):
            for b in range(a):
                t = swap(key, b, a)
                ts = fullscore(c, t)
                if ts > target:
                    target = ts
                    change = True
                    key = t
    return key

reference = clean(open("atotc.txt", "r").read())
targetQuad = quadgramstats(reference)
ctxt = clean(open("content.enc.txt", "r").read())
best = None
bb = -float("inf")
bl = -1
for L in range(1, 100):
    t = untranspose(ctxt, L)
    key = hillclimb(t)
    p = t.translate(''.maketrans(string.ascii_uppercase, key))
    bb, bl, best = max((bb, bl, best), (s := score(p), L, p))
    print(L, "=>", s)
print(bb, bl, best)
