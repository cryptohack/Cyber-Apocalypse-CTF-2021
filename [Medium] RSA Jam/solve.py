from pwn import *
import ast, math
from Crypto.PublicKey import RSA

if args.LOCAL:
    io = process(["python", "rsajam.py"])
else:
    io = remote(args.HOST, args.PORT)
    
io.recvline()
globals().update(ast.literal_eval(io.recvline().decode()))

key = RSA.construct((N, e, d))
p, q = key.p, key.q
lam = (p - 1) * (q - 1) // math.gcd(p - 1, q - 1)
d2 = pow(e, -1, lam)
if d2 == d:
    d2 += lam
io.sendline(str(d2))
io.stream()
