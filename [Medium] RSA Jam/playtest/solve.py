from Crypto.Util.number import getPrime, inverse
import random
import math

N = 149972124679038933729910401104871719527704003342511688174767463057663912878893293637082160931899636289644866247723065407706434415200444050386236170649434012119853512205291170179091748998338653531154329779729799054115250424626526702749536333790925851063122251799661382508970325427146211135297814063082697562769
e = 0x10001
d = 13407490097112915036140577690059712905882444353323709980865199292839966210803604184196169810946487770588053639095616830549948872219653046236674820694188530647175654090735448439261770331078653910070343195593996108025541447575525190221141492014750832750809709816105554995639049342528765833335030545861870330013

def challenge(d2):
    assert d2 != d
    assert 0 <= d2 < _phi

    random.seed(str(d2))
    for _ in range(50):
        m = random.randrange(N)
        c = pow(m, e, N)
        assert m == pow(c, d2, N)
    print('Winner!')

def factor_N(N,d,e):
    while True:
        k = d*e - 1
        g = random.randint(2,N-1)
        while k % 2 == 0:
            k = k // 2
        x = pow(g,k,N)
        y = math.gcd(x-1, N)
        if y > 1:
            return y, N // y

p,q = factor_N(N,d,e)

print(f'Factored N: \n\np: {p}\nq: {q}')

lam = math.lcm(p - 1, q - 1)

new_d = pow(e,-1,lam)
if new_d == d:
    new_d += lam

print(new_d)
