from pwn import *
import string

flag, quote = map(unhex, read("../release/output.txt").decode().split())
B = xor(flag, quote)[:min(len(flag), len(quote))]

while True:
    crib = input("crib> ")[:-1] # Strip off newline
    with open("log.txt", "a") as f:
        f.write(f"{crib}\n")
    for i in range(len(B) - len(crib)):
        t = xor(B[i:i+len(crib)], crib)
        if all(x in string.printable.encode() for x in t):
            print(f"{i:03d} - {t}")
