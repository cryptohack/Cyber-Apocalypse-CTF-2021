from pwn import xor

a = bytes.fromhex("08501b3dbd0fb2f7c87aeb3a224a9d568fa8ad83ff442548b5f4334f0fe1dd6b8f5d5e410be5af2d7ea642b12d8f459f2ab666d4f79a9115dc9cf22ed60e899769fd206c40819bbefe2b5a2ec592a387c6927d866b6343466d5effde0666dd3bb7f657ed651bfcf45fd5b264a36406c6b6dbb1a81272029c5e06da438a0281c19c1e10a0dc47d6ae994557e82663e9f59578")
b = bytes.fromhex("05776f0daf1ae9f6dd26e945390bad7fda889c97ff6036")

test = b"No right of private conversation was enumerated in the Constitution. I don't suppose it occurred to anyone at the time that it could be prevented."

key = xor(a, test)
print(xor(key, b))
