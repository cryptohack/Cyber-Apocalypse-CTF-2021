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

def test_transpose():
    for _ in range(100):
        n = random.randint(20,50)
        l = random.randint(1,10)
        x = ''.join(random.choice(UPPER) for i in range(n))
        c = transpose(x, l)
        p = reverse_transpose(c,l)
        assert (x==p)

def solve_transpose(input_text, L_MAX):
    scores = {}
    for l in range(1,L_MAX):
        ioc = ioc_bigrams(reverse_transpose(input_text, l))
        scores[l] = abs(ioc - bigram_ref)
    L = min(scores, key=scores.get)
    return (L, reverse_transpose(input_text, L))


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

def decode(text_input, key):
    return text_input.translate(''.maketrans(UPPER, key))

def mix_key(key):
    x, y = random.sample(range(len(key)), 2)
    key_list = list(key)
    key_list[x], key_list[y] = key_list[y], key_list[x]
    return ''.join(key_list)

def hillclimb(text_input, max_score):
    n = 0
    parent = ''.join(random.sample(UPPER,len(UPPER)))
    current = quadgram_score(decode(text_input, parent))

    while n < max_score:
        key = mix_key(parent)
        score = quadgram_score(decode(text_input, key))
        if score > current:
            n = 0
            parent = key
            current = score
        else:
            n += 1
    return decode(text_input, parent)

ref = load_file('monster.txt')
chal = load_file('content.enc.txt')
reference_fitness = fitness_dictionary(ref)

bigram_ref = ioc_bigrams(ref)
l, ct = solve_transpose(chal, 100)

while True:
    pt = hillclimb(ct, 2500)
    if 'CHTB' in pt:
        import wordsegment
        wordsegment.load()
        print(' '.join(wordsegment.segment(pt)))
        x = pt.split('CHTB')
        print('CHTB{' + x[-1] + '}')
        break





