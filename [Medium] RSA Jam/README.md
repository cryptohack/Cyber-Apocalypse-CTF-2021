# RSA jam

## Description:

* Even aliens have TLA agencies trying to apply rubber hose cryptanalysis.

## Objective:

Use the carmichael totient to find another private exponent in [0, phi(N)].

## Flag:

* See `flag.txt`

## Difficulty:

* Medium

## Release

- [rsa_jam.py](rsa_jam.py)

## Docker image

See `Dockerfile`

## Challenge

We can quickly factor `N` from the knowledge of `e` and `d`.
The quickest implementation just lets pycryptodome take care of it inside `RSA.construct`.

From there, we can calculate the carmichael totient `lambda(N) = lcm(p - 1, q - 1)`.
If we let `d2 = inverse(e, lambda(N))`, we have a valid private exponent, but it might still be equal to the original `d`.
If that is the case, we set `d2 = d + lambda(N)`.
Sending this private exponent works and gives us the flag.

## Solver

See `solve.py`.

## Playtest

Flag also found by Jack, solution in `playtest`
