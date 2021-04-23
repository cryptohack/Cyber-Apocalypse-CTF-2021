# RuneScape

## Description:

* This is an old game, and seeing how big the output file is, I understand where the M in MMO comes from...

## Objective:

Understand and implement the cryptosystem (without keygen or public key derivation).
Then to a minor bruteforce to find `theta`.

## Flag:

* See `challenge.sage`

## Difficulty:

* Hard

## Release

- [output.txt](output.txt)
- [public.sage](public.sage)
- [challenge.pdf](challenge.pdf)

## Challenge

We're given the description and most of the private key of a multivariate cryptosystem.
The only piece of the private key we're missing is $h^{-1}$, but we know that $h = q^{\theta} + 1$,
which means that we can try all possible $\theta$ to find $h$ and $h^{-1}$.
Luckily for us, we know that $q^n = q$, so our search needs to examine at most $n$ possibilities for $\theta$.

It's important to notice that we can use the private key to perform encryption too, so we don't need to perform the *very* tedious public key derivation.
We can either use the given sanity check to see if we've found the right $\theta$, or just straight away perform the xor of the "real" encryption and decryption.

There's also a little pun or joke in the PDF title.

## Solver

See `solve.sage`
  
