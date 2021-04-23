import string
from collections import Counter
import itertools
import math
import random

ALPH = string.ascii_letters
UPPER = string.ascii_uppercase

def load_file(path):
    text = open(path, 'r').read()
    return ''.join([x.upper() for x in text if x in ALPH])

def n_grams(text_input, n):
    return [text_input[i:i+n] for i in range(len(text_input)-n)]

def ioc_bigrams(text_input):
    pairs = [''.join(i) for i in itertools.product(UPPER, repeat = 2)]
    bigrams = n_grams(text_input, 2)
    N = len(bigrams)
    bigrams_counted = Counter(bigrams)
    ioc = 0
    for bi in pairs:
        ni = bigrams_counted.get(bi, 0)
        ioc += ni*(ni-1) / (N*(N-1))
    return ioc

def transpose(x, l):
    return ''.join(x[i::l] for i in range(l))

def reverse_transpose(text_input, l):
    n, r = divmod(len(text_input), l)
    padded = ''
    for _ in range(l):
        if r > 0:
            padded += text_input[:n+1]
            text_input = text_input[n+1:]
            r -= 1
        else:
            padded += text_input[:n]
            padded += ' '
            text_input = text_input[n:]
    return transpose(padded, n+1).rstrip()

def solve_block_length(text_input):
    scores = {}
    for k in range(1, K_MAX):
        text_blocks = [text_input[i::k] for i in range(k)]
        assert len(text_blocks) == k
        average_ioc = sum(ioc_bigrams(block) for block in text_blocks) / k
        scores[k] = abs(average_ioc - BI_ref)
    K = min(scores, key=scores.get)
    return K, scores[K]

def solve_K_and_L(text_input):
    scores = {}
    for l in range(1,L_MAX):
        reversed_transpose = reverse_transpose(text_input, l)
        scores[l] = solve_block_length(reversed_transpose)
    L = min(scores, key=scores.get)
    K = scores.get(L)[0]
    return K,L

def fitness_dictionary(text_input):
    quads = n_grams(text_input, 4)
    N = len(quads)
    counter_quadgrams = Counter(quads).most_common()
    # When multiplying many small probabilities, numerical underflow can occur in floating point numbers. 
    # For this reason the logarithm is taken of each probability.
    # ref: practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/
    log_scores = {quad : (math.log(score) - math.log(N)) for quad, score in counter_quadgrams}
    return log_scores

def quadgram_score(text_input):
    # Find average quad score in text
    quads = n_grams(text_input, 4)
    score = 0.0
    for q in quads:
        score += reference_fitness.get(q, -15)
    return score / len(quads)

def random_key():
    return ''.join(random.sample(UPPER, len(UPPER)))

def decode(text_input, K, keys):
    text_blocks = [text_input[i::K] for i in range(K)]
    decrypt_blocks = [text_blocks[i].translate(''.maketrans(UPPER, key)) for i,key in enumerate(keys)]
    decrypt_transpose = ''.join(decrypt_blocks)
    return reverse_transpose(decrypt_transpose, K)

def mix_key(key):
    a = random.randrange(1, 26)
    b = random.randrange(1, 26)
    if a == b:
        return key
    if a > b:
        a, b = b, a
    return key[:a] + key[b] + key[a+1:b] + key[a] + key[b+1:]

def slippery_hillclimb(text_input, K):
    # https://eprint.iacr.org/2020/302.pdf
    parent = [random_key() for _ in range(K)]
    plaintext = decode(text_input, K, parent)
    bestfit = quadgram_score(plaintext)

    bestkey = parent
    big_count = 0
    while big_count < BIG_LIMIT:
        print('Again?')
        for i in range(K):
            parent[i] = random_key()
            plaintext = decode(text_input, K, parent)
            parentfit = quadgram_score(plaintext)
            small_count = 0

            while small_count < SMALL_LIMIT:
                child = parent[:i] + [mix_key(parent[i])] + parent[i+1:]
                # child = parent
                # child[i] = mix_key(child[i])
                plaintext = decode(text_input, K, child)
                childfit = quadgram_score(plaintext)

                if childfit > parentfit:
                    parent = child
                    parentfit = childfit
                    small_count = 0
                else:
                    small_count += 1

                if childfit > bestfit:
                    print(f'Getting better: {childfit}')
                    bestfit = childfit
                    bestkey = child
                    big_count = 0
                else:
                    big_count += 1

    return decode(text_input, K, bestkey)

L_MAX = 20
K_MAX = 20

ref = load_file('monster.txt')
chal = load_file('content.enc.htb.txt')
reference_fitness = fitness_dictionary(ref)

print(f'Target fitness: {quadgram_score(ref)}')

BI_ref = ioc_bigrams(ref)
K, L = solve_K_and_L(chal)
print(f'K={K}, L={L}')

ciphertext = reverse_transpose(chal, L)
SMALL_LIMIT = 1000
BIG_LIMIT = (5000000*K**2) // len(ciphertext)

# pt = slippery_hillclimb(ciphertext, K, SMALL_LIMIT, BIG_LIMIT)
pt = slippery_hillclimb(ciphertext, K)
print(pt)




