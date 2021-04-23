load("challenge.sage")

print(f"Base field F_q = {F}")
print(f"defined by {F.modulus()}")
print()

print(f"Extension field K, including modulus: {K}")
print()

pub, priv = keygen()
for i, fi in enumerate(pub):
    print(f"f_{i}: {fi}")
print()

L1, L2, h_inv = priv
print(f"M1: {list(L1[0])}")
print(f"k1: {L1[1]}")
print()
print(f"M2: {list(L2[0])}")
print(f"k2: {L2[1]}")
print()

def byte_to_F(b):
    return sum(int(bit) * alpha^i for i, bit in enumerate(bin(b)[2:].zfill(8)[::-1]))

def bytes_to_V(b):
    assert len(b) <= n
    b += b"\0" * (n - len(b))
    return vector(F, [byte_to_F(x) for x in b])

def xor(a, b):
    return bytes(x ^^ y for x, y in zip(a, b))

print("a sanity check:")
print(decrypt(priv, bytes_to_V(b"\x01" * n)))
print(encrypt(pub, bytes_to_V(b"\x01" * n)))
print()

import secrets
k = secrets.token_bytes(len(FLAG))
print(f"an encryption: {encrypt(pub, bytes_to_V(k))}")
print(f"a decryption: {decrypt(priv, bytes_to_V(xor(k, FLAG)))}")
print()
