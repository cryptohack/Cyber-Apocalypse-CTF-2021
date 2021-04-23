from Crypto.Util.number import long_to_bytes
with open("../output.txt") as f:
    l = f.read().splitlines()
    p = int(l[0].split(" = ")[1])
    c1 = int(l[1].split(" = ")[1])
    c2 = int(l[2].split(" = ")[1])
def decrypt(c, key):
    d = int(pow(0x10001, -1, E.order()))
    P = E.lift_x(F(int(c) ^^ int(key)))
    return (d*P)[0]
F = GF(p)
E = EllipticCurve(F, [1, 2])
print(long_to_bytes(decrypt(c1, 0)) + long_to_bytes(decrypt(c2, E.j_invariant())))
