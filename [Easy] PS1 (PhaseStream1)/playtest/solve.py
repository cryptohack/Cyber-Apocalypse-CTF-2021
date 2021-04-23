from pwn import xor, unhex
t = unhex('2e313f2702184c5a0b1e321205550e03261b094d5c171f56011904')
print(xor(t, t[:5], 'CHTB{'))
