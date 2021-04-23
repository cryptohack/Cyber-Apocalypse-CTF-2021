from pwn import *

for l in read("../release/output.txt").decode().strip().splitlines():
    try:
        t = unhex(l)
        s = xor(t, t[0], 'C').decode()
        if s.startswith("CHTB"):
            print(s)
    except: pass
