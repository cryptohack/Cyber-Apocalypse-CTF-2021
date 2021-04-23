# Super Metroid

## Description:
Samus needs our help! After a day of burning out her Arm Cannon, blasting Metroids and melting the Mother Brain, she's found her ship's maps have all been encrypted. Lucky for her, these aliens still don't know what they're doing and are trying to roll their own crypto. Can you recover the flag from their elliptic protocol?

## Objective:
* RSA is undone using order of the curve
* The key is the j invariant of the curve

## Difficulty:
* `Medium`

## Flag:
* See flag.txt

## Release:
* `release.zip` has the challenge script and the encrypted flag.

## Challenge:

To undo the "RSA" encryption, we only need the order of the curve, which is efficently computed using Schoof's algorithm.

For SageMath, we simply call

```py
F = GF(p)
E = EllipticCurve(F, [1,2])
n = E.order()
```

The key is the j invariant of the curve of `E1`. As `E` is isomorphic to `E1`, the j-invariant is the same for both and we can solve very quickly.

See `solve.sage` for a full solution.

## Playtest

Flag also found by Robin, solution in `playtest`.
