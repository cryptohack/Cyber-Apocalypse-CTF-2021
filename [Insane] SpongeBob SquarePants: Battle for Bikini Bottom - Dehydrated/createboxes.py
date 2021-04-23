import random

random.seed(0x1337 ^ 0x4242)

FIXED_BITS = [2, 4, 5]
C = 10
B = 8

PBOXES = [list(range(C + B)) for _ in range(8)]
for p in PBOXES:
    random.shuffle(p)
print(f"{PBOXES = }")

unfixed = []
fixed = []
for n in range(256):
    if all((n & (1 << b)) == 0 for b in FIXED_BITS):
        fixed.append(n)
    else:
        unfixed.append(n)
random.shuffle(fixed)
random.shuffle(unfixed)
a, b = 0, 0
SBOX = []
for n in range(256):
    if n in fixed:
        SBOX.append(fixed[a])
        a += 1
    else:
        SBOX.append(unfixed[b])
        b += 1
print(f"{SBOX = }")
INIT = []
for _ in range(B):
    INIT.append(random.choice(range(256)))
for _ in range(C):
    INIT.append(random.choice(fixed))
print(f"{INIT = }")
