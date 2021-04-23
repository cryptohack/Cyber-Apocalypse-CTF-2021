def string_to_sage(maths):
    return eval(preparse(maths.strip()))

def file_to_sage(line_number, split_str):
    maths_string = data[line_number].split(split_str)[-1]
    return string_to_sage(maths_string)

def from_V_to_bytes(V):
    bs = []
    for x in V:
        bs.append(x.integer_representation())
    return bytes(bs)

def xor_bytes(b1, b2):
    return bytes([a^^b for a,b in zip(b1,b2)])

# Read the file as lines (string)
with open('output.txt') as f:
    data = f.readlines()

# Construct element x of field GF(2)
x = GF(2)['x'].gen()

# Use this to create F_2^8 with a basis element called alpha to match output
modulus = x^8 + x^4 + x^3 + x^2 + 1
F.<alpha> = GF(2^8, name="alpha", modulus=modulus)

# Now make a polynomial ring with X as the generator
R.<X> = F['X']

# this polynomial is a mess, so we pull it from the file
irr_poly = file_to_sage(3, ' 2^8 with modulus ')

# Finally, we get our extension field K by taking the modulo
K.<X> = R.quotient_ring(irr_poly)

n = irr_poly.degree()
assert n == 60 # match with statement in Section 4


"""
To solve this, we need to take elements from output and encrypt AND
decrypt them. Lets start by definining our functions
"""

"""
The function phi, phi inverse can be computed from our basis
"""
beta = [X^i for i in range(n)]

"""
We need this to add zeros as x.list() only gives up to highest order (annoying)
"""
def pad_list_x(x):
    return x.list() + [0]*(n - len(x.list()))

"""
Okay, now we can define phi and its inverse
"""
# phi: K -> V
def phi(x):
    return vector(F, pad_list_x(x))

# phi^-1: V -> K
def phi_inv(a_vec):
    return sum(a*b for a, b in zip(a_vec, beta))

"""
The function psi is just exponentiation, easy peasy
Note that we pick h s.t. h_inv exists :)
"""
# psi: K -> K
def psi(u):
    return u^h

# psi^-1: K -> K
def psi_inv(u):
    return u^h_inv

"""
The L functions can be computed directly from M, k which
we are given in output.txt
"""
def L1(x):
    return M1 * x + k1

def L1_inv(x):
    return M1.inverse() * (x - k1)

def L2(x):
    return M2 * x + k2

def L2_inv(x):
    return M2.inverse() * (x - k2)


"""
Putting this all together we can write the excryption function
This is the function f given at the top of page 2

f: K -> K
"""
def encrypt(x):
    tmp = L1(x)
    tmp = phi_inv(tmp)
    tmp = psi(tmp)
    tmp = phi(tmp)
    return L2(tmp)

"""
We can just do this backwards to decrypt
"""
def decrypt(y):
    tmp = L2_inv(y)
    tmp = phi_inv(tmp)
    tmp = psi_inv(tmp)
    tmp = phi(tmp)
    return L1_inv(tmp)
    

"""
Now all we have to do is extract the private key and flag from the file
"""

# Private key is made from (h, M1, k1, M2, k2)
# We are given M1, M2, k1, k2 which we can extract
M1 = file_to_sage(66, 'M1: ')
M1 = Matrix(F, M1)
k1 = file_to_sage(67, 'k1: ')
k1 = vector(F, k1)

M2 = file_to_sage(69, 'M2: ')
M2 = Matrix(F, M2)
k2 = file_to_sage(70, 'k2: ')
k2 = vector(F, k2)

# The flag is split between two files which are encrypted and decrypted
# Lets grab the two pieces
flag_encrypted = file_to_sage(76, 'an encryption: ')
flag_encrypted = vector(F, flag_encrypted)

flag_decrypted = file_to_sage(77, 'a decryption: ')
flag_decrypted = vector(F, flag_decrypted)



q = 2^8
for theta in range(2,n):
    h = q^theta + 1
    """
    h inverse must exist, so we must have that h is coprime to the group order
    """
    if gcd(h, q^n - 1) != 1:
        continue

    print(f'Guessing theta = {theta}')
    h_inv = inverse_mod(h, q^n - 1)

    k = decrypt(flag_encrypted)
    k_xor_flag = encrypt(flag_decrypted)

    k_bytes = from_V_to_bytes(k)
    k_xor_flag_bytes = from_V_to_bytes(k_xor_flag)

    print(xor_bytes(k_bytes, k_xor_flag_bytes))

