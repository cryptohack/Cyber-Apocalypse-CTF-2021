# SpongeBob SquarePants: Battle for Bikini Bottom – Dehydrated

## Description:

* Just added a bit more water this time. The sponge sucked it all up.

## Objective:

Find the backdoor in the sponge function, use it to create a collision in the sponge capacity thanks to the birthday paradox, use that to create a full collision.

## Flag:

* See `flag.txt`

## Difficulty:

* Insane

## Release

- [spongebob.py](spongebob.py)

## Docker image

See `Dockerfile`

## Challenge

Inspecting the source code given, we see a sponge function used as a hash function.
Our goal is to create a collision for it, and obtain the flag.

The sponge does the following for each block of the message:

- Apply a bitwise xor between the bitrate of the state and the message
- For 8 rounds:
    - Permute the bits of the entire state, each bit stays at the same "bit index", but the bytes to which they belong are permuted
    - Perform a substitution step for every byte of the state

The final state is then the hash value.

First, observe that finding two messages that collide in the capacity allows us
to find two fully colliding messages by appending just a single block to each.
Since the capacity is the same for both after the first blocks, we simply append two blocks that
xor to the difference between the two bitrates at that point, and since a block is only mixed in once,
that means that the final states will still entirely match.

Since the capacity of the sponge consists of 10 bytes, we expect to need about 2^40 hashes to have a birthday attack on the collision.
This *might* be feasible within the time limits, but even a small mess up or a lack of memory
will easily lead to a failure here.
Instead, we can figure out that the construction is backdoored, by starting to ask ourselves the question "why are bits only permuted at a fixed index".
From there, if we further investigate the SBOX (and we can for example inspect the cycle decomposition of this permutation),
we can discover the horrible secret: if the bits at index 2, 4, and 5 are all 0, they remain that way.
These bits then further remain invariant after permutation too, as they remain at the same index.

The initial state has the correct bits fixed in the capacity, but not in the bitrate.
As such, we also introduce a first block that will map the bitrate part to have the wanted fixed bits too.
So, if we ensure that the bits 2, 4, and 5 will always remain 0, in this case by making sure
our message blocks also have 0s at those indices, we have reduced the security of this hash function
from `10*8/2 = 40` bits to `10*5 / 2 = 25` bits only.
This brings it well in range of a birthday attack.

Implementing this in plain python will be very slow, but already running it in pypy instead will provide a
significant speedup. It should also be possible to implement it in a compiled language for potentially even greater speeds.

## Solver

See `solve.py` (best run in pypy).
