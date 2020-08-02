import binascii
import string

def decrypt(lastchar, DEBUG=True):
	# Get encrypted flag
	with open("out.out", "rb") as f:
		contents = f.read()

	encrypted_flag = list(map(int, ''.join('{0:08b}'.format((x), 'b') for x in contents)))
	if DEBUG: print(encrypted_flag)
	if DEBUG: print(len(encrypted_flag))

	# Get shift register outputs state for the first 64 bits
	plain_flag = "WH2020{" + lastchar
	plain_flag = list(map(int, ''.join('{0:08b}'.format(ord(x), 'b') for x in plain_flag)))

	state = ''
	for i in range(64):
		out = encrypted_flag[i] ^ plain_flag[i]
		state = state + str(out)
	if DEBUG: print('state', state)

	state = int(state, 2)
	if DEBUG: print('state', state)

	# LSFR class
	class LSFR:
	    def __init__(self, state, taps, length):
	        self.taps = taps
	        self.state = state
	        self.length = 2**length

	    def getNext(self):
	        out = 0
	        xored = self.taps & self.state
	        while xored > 0:
	            if xored % 2 == 1:
	                out = 1 - out
	            xored //= 2
	        self.state = (self.state*2 + out)%self.length
	        return out

	# Make the single LSFR
	shiftregister = LSFR(state, 15564440312192434176, 64);

	# Then decode each bit onwards
	flag = ''
	for enc in encrypted_flag[64:]:
		out = shiftregister.getNext() ^ enc
		flag = flag + str(out)

	if DEBUG: print(flag)

	n = int(flag, 2)
	decoded = binascii.unhexlify('%x' % n)
	if DEBUG: print(decoded)

	return decoded

# Test
print(decrypt('A', DEBUG=True))

# Bruteforce last char so we have 8 characters total to form the 64-bit state
for ch in string.printable:
	prefix = "WH2020{" + ch
	output = decrypt(ch, DEBUG=False)
	print(ord(ch), prefix.encode() + output)
