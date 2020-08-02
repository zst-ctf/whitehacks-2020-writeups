#!/usr/bin/env python3
from Crypto.PublicKey import RSA
from Crypto.Util import asn1
from base64 import b64decode
import binascii
import gmpy2

# Read in: n, e, c
exec(open('vals.txt').read())

# Get from FactorDB: p, q
p = 757797040104296557573809656933
q = 927584008074066047910168872563

# Compute phi
phi = (p-1) * (q-1)

# Compute modular inverse of e
d = int(gmpy2.invert(e, phi))

# Decrypt
priv_key = RSA.construct((n, e, d))
# m = priv_key.decrypt(c)
# pow(c, d) % n
m = pow(c, d, n)

# https://stackoverflow.com/questions/4368676/is-there-a-way-to-pad-to-an-even-number-of-digits
def hex_pair(x):
    return ('0' * (len(x) % 2)) + x

# Decode to ASCII
m_hex = '{:x}'.format(m)
m_hex = hex_pair(m_hex)
msg = binascii.unhexlify(m_hex)
print(msg)
