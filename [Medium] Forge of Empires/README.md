# Forge of Empires

## Description:
Over thousands of miles, a messenger from the East has arrived with the sacred text. To enable `PHOTON MAN` and crush the aliens with your robot troopers, the messenger needs you to sign your message!

## Objective:
* forge a message using that the signing scheme does not hash the message

## Difficulty:
* `Medium`

## Flag:
* See flag.txt

## Release:
* Dynamic challenge, source should be given to the user, which is a single python file in `release.zip`

## Challenge:

![description of solution](https://github.com/cryptohack/chtb/blob/0396fef17f4aeed4f324d78f2a0f63eb5efe12cc/%5BMedium%5D%20Forge%20of%20Empires/Screenshot%202021-04-11%20at%2012.52.01%20pm.png)

As we do not hash the message, we can hand-pick `m` such that the message is correctly signed. A full implementation is given in `solve.py`

## Playtest

Flag found by Robin, solution in playtest
