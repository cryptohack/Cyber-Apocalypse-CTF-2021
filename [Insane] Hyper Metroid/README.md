# Hyper Metroid

## Description

Dropping a morph ball bomb, Samus cracked open the floor and dropped down into the guts of Phaaze. At the end of the tunnel is a locked chest containing the hyper beam upgrade. Samus found the encrypted key preserved in a ball of glowing biomass, but can't decode it. Help Samus capture the flag so she can eradicate the alien invasion once and for all. 

## Objective:
The prime `p` is of a special form, which allows us to quickly solve for the order of the Jacobian.

## Difficulty:
* `Insane`

## Flag:
* See flag.txt

### Release:
Challenge is comprised of the sage file `hyper-metroid.sage` and the output `output.txt`. This has been zipped into `release.zip`.

### Challenge:

This challenge uses that the prime is a generalised Mersenne prime. The curve itself is a twisted hyperelliptic curve.

We can solve this challenge from the below reference

![Screenshot from Koblitz](https://github.com/cryptohack/Cyber-Apocalypse-CTF-2021/blob/841628c497b31ccb16947c09137685de2b2ceefe/%5BInsane%5D%20Hyper%20Metroid/Screenshot%202021-03-12%20at%205.57.53%20pm.png)

A full implementation of this challenge is given in `solve.sage`

## Playtest

Flag also found by Robin in a playtest within `playtest`.
