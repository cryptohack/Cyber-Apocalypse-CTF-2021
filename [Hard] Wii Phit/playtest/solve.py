# After a transformation:
# 1/x + 1/y - 1/z = 4/w
# Searching for 'sum reciprocals 4 diophantine' leads to https://en.wikipedia.org/wiki/List_of_sums_of_reciprocals
# Where in turn, we can find "The Erdős–Straus conjecture states that for all integers n ≥ 2, the rational number 4/n can be expressed as the sum of three reciprocals of positive integers."
# Which leads us to a solution with one negative term
# {\displaystyle {\frac {4}{n}}={\frac {1}{(n-1)/2}}+{\frac {1}{(n+1)/2}}-{\frac {1}{n(n-1)(n+1)/4}}.}

from Crypto.Util.number import *

w = 25965460884749769384351428855708318685345170011800821829011862918688758545847199832834284337871947234627057905530743956554688825819477516944610078633662855
# x = p + 1328
# y = p + 1329
# z = q - 1
z = w * (w - 1) * (w + 1) // 4
q = z + 1
x = (w - 1) // 2
p = x - 1328

n = p**3 * q

phi = p**2 * (p - 1) * (q - 1)
with open("../output.txt") as f:
    f = int(f.read().split()[1], 16)
e = 0x10001
d = pow(e, -1, phi)
print(long_to_bytes(pow(f, d, n)))
