# Tetris

## Description:

* It seems the aliens might be living backwards in time, so now we're suddenly seeing completely different and older kinds of cipher too.
* The flag consists entirely of uppercase characters, and is of the form `CHTB{SOMETHINGHERE}`. You'll still have to insert the `{}` yourself.

## Objective:

Figure out and undo the correct transposition length, then solve the monoalphabetic substitution.

## Flag:

* See `flag.txt`

## Difficulty:

* Medium

## Release

- [content.enc.txt](content.enc.txt)
- [tetris.py](tetris.py)

## Challenge

The encryption happens in two steps, which we will undo in reverse order.
First it applies a random monoalphabetic substitution, then it applies an unkeyed transposition of a random length.

To undo the transposition, we need to figure out its length.
Assume we know the length `L`, then we can easily undo the transposition by dividing the ciphertext in
`L` blocks and interleaving them.
Since `L` comes from a limited space, we can try all of them, either seeing if we can get a reasonable
plaintext when trying to solve the substitution, or by doing a different kind of detection.
The detection we opt for, is evaluating the average distance of the *Index of Coincidence* (IoC) to a target
IoC derived from some arbitrary english language reference text.

Once we find the correct `L`, we can either use some tool like https://quipqiup.com to undo the substitution,
or we can write our own algorithm.
When writing our own, we opt to use a hill climbing approach, where the fitness score is derived from the quadgram statistics.
We could attempt to write a clever fitness function for this based on e.g. the chi-squared test,
but simply taking a sum in log-space with an aptly chosen fallback for "impossible" quadgrams gives us good results

## Solver

See `solve.py`
  
