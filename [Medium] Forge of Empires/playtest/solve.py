from pwn import *
from Crypto.Util.number import bytes_to_long

p = 2**1024 + 1657867
g = 3
MASK = (2**p.bit_length() - 1)

def forge(y):
    e = 2
    r = (pow(g, e, p) * y) % p
    s = (-r) % (p - 1)
    return (e * s) % p, r, s

def embed(m, extra):
    extra = bytes_to_long(extra)
    return (extra << 8*((p.bit_length() + 23) // 8)) | m

if args.LOCAL:
    io = process(['python', '../forge_of_empires.py'])
else:
    io = remote(args.HOST, args.PORT)


io.recvuntil("public key: ")
pub = int(io.recvline())
m, r, s = forge(pub)
print(m, r, s)
io.sendline(hex(embed(m, b"get_flag"))[2:])
io.sendline(str(r))
io.sendline(str(s))

io.stream()
