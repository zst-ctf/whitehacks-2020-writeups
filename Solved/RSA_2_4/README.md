# RSA 2/4
Crypto

## Challenge 
DESCRIPTION
Let's kick it up a notch. Bob generated these RSA parameters and was certain that his encryption would be unbreakable because his smartest friend (John) couldn't crack it. Is it truly secure?

Download vals.txt and decrypt the value of c given all the other params.

Author: lord_idiot


ATTACHED FILES
vals.txt

## Solution

Use factordb to get p and q.

	p = 757797040104296557573809656933
	q = 927584008074066047910168872563

[decrypt_rsa2.py](decrypt_rsa2.py)

## Flag

	WH2020{B1gg3r_primes!}