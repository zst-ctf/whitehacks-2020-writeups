#!/usr/bin/env python3
from Crypto.PublicKey import RSA
from Crypto.Util import asn1
from base64 import b64decode
import binascii

# Read in: n, e, c, p, q, d
exec(open('vals.txt').read())

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
