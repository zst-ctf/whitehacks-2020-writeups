#!/usr/bin/env python3
from Crypto.PublicKey import RSA
from Crypto.Util import asn1
from Crypto.Util.number import *
from base64 import b64decode
import binascii
import gmpy2

# Read in: n, e, c
exec(open('vals.txt').read())

# Keep adding N until we have a solution
ct = c
for k in range(10000):
    potential_pt, is_cube = gmpy2.iroot(ct + (k * n), e)
    if is_cube:
        print(i, long_to_bytes(potential_pt))
