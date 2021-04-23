# Little Nightmares

## Description

Never in your darkest momements did your childhood fears prepare you for an alien invasion. To make matters worse, you've just been given a Little homework by the Lady. Defeat this and she we retreat into the night.

## Objective
* Factor `N` and decrypt the flag using Fermat's little theorem

## Flag
* See `flag.txt`

## Difficulty
* `Medium`

## Release
* `release.zip` which has the encrypted flag in `output.txt` and the challenge source in `little-nightmares.py`

## Challenge

The factors `p,q` can be found by looking at:

```py
p = math.gcd(g1 - 1, N)
q = math.gcd(g2 - 1, N)
```

where we use that `g^(p-1) mod p = 1` and so `g^(p-1) mod N = 1 + k*p` for some integer `k`. 

The challenge gives the decrypt function for free, so these values make the private key and the challenge is solved.

## Playtest

Flag also found by Robin, solution in `playtest`
