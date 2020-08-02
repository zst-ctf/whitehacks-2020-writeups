# RSA 3/4
Crypto

## Challenge 

	This is bill
	bill does not pad his messages
	Bill is dumb
	dont be like bill

Download vals.txt and decrypt the value of c given all the other params.

Author: lord_idiot

ATTACHED FILES
vals.txt

## Solution

No padding means that `m^e` may be small.

So given that `C = m^e (mod n)`,

Then we know `C + kn = m^e`, where k is a small number.

So make a simple script to loop through k until we can have the root which is the flag

[decrypt_rsa3.py](decrypt_rsa3.py)

## Flag

	WH2020{Pl3as3_r3memBer_to_pAD_ur_RSA_m3ssag3s!}
