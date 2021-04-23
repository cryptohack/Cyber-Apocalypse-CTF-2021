# Tetris 3D

## Description:

* With all the timey-wimey weirdness going on, I have no idea if the aliens encrypted this before or after the tetris game. All I know is that I want my games back!
* The flag consists entirely of uppercase characters, and is of the form `CHTB{SOMETHINGHERE}`. You'll still have to insert the `{}` yourself.

## Objective:

Figure out and undo the correct transposition length, then solve the periodic polyalphabetic substitution.

## Flag:

* See `flag.txt`

## Difficulty:

* Insane

## Release

- [content.enc.txt](content.enc.txt)
- [tetris_3d.py](tetris_3d.py)

## Challenge

The encryption happens in two steps, which we will undo in reverse order.
First it applies `K` random monoalphabetic substitutions, periodically.
Then it applies an unkeyed transposition of a random length `L`.

This solution follows a similar spirit to the solution for tetris, but is significantly trickier.

We start of by figuring out the correct values for `K` and `L`.
To achieve this, we again look at the *Index of Coincidence* (IoC).
Different from tetris however, is that we have to make sure that our measurements
don't mix ciphertext corresponding to different substitutions.
So what we will do is as before: we try all possible `L` and undo the corresponding transposition.
Then we try all possible `K`, and calculate the average IoC over all `K` parts of the ciphertext,
each corresponding to a single substitution.
When we take the distance to our reference IoC as before, we can cleanly observe the correct values.
Note that we might also observe some multiples of `K` as giving good results, since that corresponds
to a repetition of the sequence of substitutions.

To solve the substitution ciphers, we again resort to a hillclimbing approach.
It is similar to the technique set out in [Slippery hill-climbing technique for ciphertext-only cryptanalysis of periodic polyalphabetic substitution ciphers](https://eprint.iacr.org/2020/302.pdf) by Thomas Kaeding.
Our fitness score will be the same as before: a sum of log-space frequencies.
Differently from before, we can't solve a single substitution at once, as they can't form proper quadgrams.
Instead, we will score the entire plaintext, covering all keys together.
We improve each single substitution individually, starting from a random key, while keeping the others fixed.
If we repeat this process enough, to make sure our randomness did not accidentally miss an improvement,
this will very frequently find the correct solution, without getting stuck in local optima.
This "reset" of a single substitution is what makes the hillclimbing *slippery* as in the title of the referenced paper.
This form of optimization, where we find an optimum when changing a single part of the solution,
while keeping everything else fixed, is commonly seen in other areas as well.

It might also be possible to solve the substitutions with some more manual work after assigning the closest
matching reference frequencies as initial keys and performing manual improvements and attempting some crib dragging,
but due to the sheer tedium involved, we did not attempt this ourselves.

## Solver

See `solve.py` and `hillclimber.cpp`.
