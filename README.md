# CyberApocalype Crypto Challenges

> The aliens have encrypted all our games to try and force us to be productive and make us miserable. Fortunately, the aliens haven't played CryptoHack so don't know how to make a strong cipher. Can you recover our games, consoles, and flags?

## Challenge Breakdown

We were asked to estimate challenge difficulty for the challenges we made, which are broken down below. For a full discussion of the challenges with intended solution, see our [blog post]()

Thanks for playing CHTB!

- Hyperreality, Robin, Jack

### "Easy": ⭐

- Nintendo Base64: base64 flag several times, ciphertext is nice N64 ASCII art
- PS (PhaseStream): XOR repeated key cipher
- PS2 (PhaseStream 2): file with 100,000 random data lines and one has been XORd with a single byte key
- PS3 (PhaseStream 3): re-used stream cipher key
- Soulcrabber: Rust RNG initialised with constant value

### "Medium": ⭐⭐

- PS4 (PhaseStream 4): re-used stream cipher with crib-dragging
- Soulcrabber II: Rust RNG initialised with current time
- RSA Jam: Simple RSA chal where you need to find a "second" private exponent, i.e. by using carmichael lambda
- Super Metroid: RSA Elliptic Cruve mix, with order of curve and j-invariant as things to learn
- Forge of Empires: Forgery of Elgamal signatures without hash functions
- Tetris: monoalphabetic substitution cipher (with some minor transposition to resist quipqiup)
- Little Nightmares: factor the modulus by using GCD and fermat's "little" theorem

### "Hard": ⭐⭐⭐

- WiiPhi: RSA with p^3 * q with Erdős-Straus conjecture diophantine question

### "Very Hard": ⭐⭐⭐⭐

- RuneScape: Imai-Matsumoto implementation
- Hyper Metroid (find the order of the Jacobian of a hyperelliptic curve using that p is a generalised Mersenne prime)
- Tetris 3D: periodic polyalphabetic substitution cipher (with some minor transposition)
- SpongeBob SquarePants: Battle for Bikini Bottom – Rehydrated: Backdoored sponge function hash collision
