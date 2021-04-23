# Solve
from Crypto.Util.number import long_to_bytes

p = 103286641759600285797850797617629977324547405479993669860676630672349238970323
c1 = 39515350190224022595423324336682561295008443386321945222926612155252852069385
c2 = 102036897442608703406754776248651511553323754723619976410650252804157884591552

F = GF(p)
E = EllipticCurve(F, [1,2])

n = E.order()
d = inverse_mod(0x10001, n)
key = int(E.j_invariant())

P1 = E.lift_x(Integer(c1))
P2 = E.lift_x(Integer(c2^^key))

G1 = d*P1
G2 = d*P2

flag = long_to_bytes(int(G1[0])) + long_to_bytes(int(G2[0]))
print(flag)