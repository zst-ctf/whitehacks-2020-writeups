# Concatacollision
Crypto

## Challenge 

DESCRIPTION
To print the flag, looks like we need a 2FA token to verify. Although we have no token, our engineers have managed to secure the code of the checking server. I'm sure the check function isn't as secure as they think...

nc chals.whitehacks.ctf.sg 10001
Author: prokarius

ATTACHED FILES
concat.py


## Solution

workings

	return int(str(int(str(x1) + s) % x0) + s) % x1 == 1


	A2 + L*x0 = (x1 * (10**concat_exp)) + concat_numb
	K*x1 + 1 = (A2 * (10**concat_exp)) + concat_numb


	(K*x1 + 1 - concat_numb) / (10**concat_exp) + L*x0 = (x1 * (10**concat_exp)) + concat_numb
	(K*x1 + 1 - concat_numb) / (10**concat_exp) = (x1 * (10**concat_exp)) + concat_numb - L*x0 
	(K*x1 + 1 - concat_numb) = (x1 * (10**concat_exp))*(10**concat_exp) + concat_numb*(10**concat_exp) - L*x0*(10**concat_exp) 
	(K*x1 + 1 - concat_numb) - concat_numb*(10**concat_exp) = (x1 * (10**concat_exp))*(10**concat_exp) - L*x0*(10**concat_exp) 

	K*x1 + 1 - concat_numb*(10**concat_exp + 1) = (x1 * (10**concat_exp))*(10**concat_exp) - L*x0*(10**concat_exp) 

int(str(x1) + s) % x0) + s) % x1 == 1

## Flag

	?