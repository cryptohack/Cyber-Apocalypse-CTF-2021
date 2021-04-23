# Wii Phit

## Description:

The aliens have encrypted our save file from Wii Phit and we're about to lose our 4,869 day streak!! They're even taunting us with a hint. I think the alien's are getting a bit over-confident if you ask me.

## Objective:

* Standard RSA, except N = p^3 * q such that phi = p^2(p-1)(q-1)
* Primes found from diophantine equation

## Difficulty:
* `Hard`

## Flag:
* See flag.txt

## Release:
Challenge is comprised of `wii-phit.py` and `output.txt` which are in `release` and zipped into `release.zip`

## Challenge:

p,q can be solved by noticing that

4 / n = 1/x + 1/y - 1/z

Which is associated to the Erdos-Straus-Conjecture and has solutions of the form

4 / n = 1 / k + 1 / (k+1) - 1 / k(k+1)(2k+1)

for n = 2k + 1

The rest of the solution is trivial and shown in `solve.py`

## Playtest

Flag also found by Robin in a playtest within `playtest`.