#!/usr/bin/env python3
import gmpy2
import socket
import telnetlib
import struct
import sympy

# LCG solver
def lcg(m, a, c, x=0):
    return (a * x + c) % m

def rlcg(m, a, c, x=0):
    ainv = gmpy2.invert(a, m)
    return ainv * (x - c) % m

def solve_a(lcg0, lcg1, lcg2, m):
    a = (lcg2 - lcg1) * gmpy2.invert(lcg1 - lcg0, m) % m
    return a

def solve_c(lcg0, lcg1, m, a):
    c = (lcg1 - a * lcg0) % m
    return c


shipgirls = [
    "Aulick", "Beagle", "Benson", "Bulldog", "Cassin", "Comet", "Craven", "Crescent", "Cygnet", "Downes", "Foote", "Foxhound", "Kisaragi", "McCall", "Mikazuki", "Minazuki", "Mutsuki", "Shiranui", "Spence", "Uzuki", "Z20", "Z21",
    "Acasta", "Akatsuki", "Amazon", "Arashio", "Ardent", "Ariake", "Asashio", "Aylwin", "Bache", "Bailey", "Bush", "Dewey", "Echo", "Fletcher", "Forbin", "Fortune", "Fumizuki", "Gridley", "Halsey Powell", "Hamakaze", "Hammann", "Hatakaze", "Hatsuharu", "Hatsushimo", "Hazelwood", "Hobby", "Ikazuchi", "Inazuma", "Isokaze", "Jenkins", "Jersey", "Juno", "Jupiter", "Kagerou", "Kalk", "Kamikaze", "Kimberly", "Kiyonami", "Kuroshio", "Le Mars", "Matsukaze", "Michishio", "Mullany", "Nagatsuki", "Ooshio", "Oyashio", "Radford", "San Juan", "Shiratsuyu",
    "Sims", "Smalley", "Stanly", "Tanikaze", "Thatcher", "Urakaze", "Wakaba", "Yuugure", "Z18", "Z19", "Z36",
    "An Shan", "Ayanami", "Carabiniere", "Chang Chun", "Charles Ausburne", "Cooper", "Fu Shun", "Fubuki", "Glowworm", "Grenville", "Grozny", "Hanazuki", "Harutsuki", "Hibiki", "Javelin", "Kasumi", "L Opiniatre", "Laffey", "Le Temeraire", "Makinami", "Matchless", "Maury", "Minsk", "Musketeer", "Naganami", "Nicholas", "Niizuki", "Nowaki", "Shigure", "Tai Yuan", "Tartu", "Universal Bulin", "Uranami", "Vampire", "Vauquelin", "Yoizuki", "Z1", "Z23", "Z25", "Z35",
    "Eldridge", "Kawakaze", "Le Malin", "Le Triomphant", "Prototype Bulin MKII", "Tashkent", "Yudachi", "Yukikaze", "Z46"
]
# print(len(shipgirls))

def main():
	def p64(x):
	    return struct.pack('<Q', x)

	# Connect to program
	s = socket.socket()
	s.connect(('chals.whitehacks.ctf.sg', 10002))
	t = telnetlib.Telnet()
	t.sock = s

	# Modulus
	m = len(shipgirls)

	# Get samples
	samples = []
	for i in range(m * 10):
		t.read_until(b'waifu?')
		t.write(b'idk\n')

		t.read_until(b'waifu is ')

		waifu = t.read_until(b'\n').decode().strip()
		waifu_index = shipgirls.index(waifu)
		print(waifu, waifu_index)

		samples.append(waifu_index)

	# https://scicomp.stackexchange.com/a/1534
	print(samples)

	quit()
	samples


	# Find parameters
	a = solve_a(samples[0], samples[1], samples[2], m)
	c = solve_c(samples[0], samples[1], m, a)
	print(f'Found parameters:')
	print(f'>> m: {m}')
	print(f'>> a: {a}')
	print(f'>> c: {c}')
	print()

	# LCG class
	class LCG():
	    def __init__(self, mod, a, v): 
	        # Mod should be a prime number
	        while not sympy.isprime(mod):
	            mod -= 1
	            if mod == 1:
	                print("You done messed up good")
	                raise Exception

	        self.a = a
	        self.v = v
	        self.mod = mod
	        self.counter = 0

	    def next_bag(self):
	        self.v += self.a
	        self.value = 1

	    def get_next(self):
	        if self.counter == 0:
	            self.next_bag()
	            self.counter = self.mod // 2

	        self.value = (self.a * self.value + self.v) % self.mod
	        self.counter -= 1
	        return self.value

	lcg_class = LCG(m, a, c)

	# Check guesses
	print(f'Doing guesses:')
	lcg_last = samples[0]
	for i in range(len(samples)):
		orig = samples[i]
		#predicted = lcg_class.get_next()
		predicted = lcg(m, a, c, lcg_last)
		print(orig, predicted)
		lcg_last = predicted
		
	quit()



	lcg_last = lcg_3
	for x in range(30):
		lcg_last = lcg(mod_value, a, c, lcg_last)
		print(f'>> next {x}: {lcg_last}')
		guess(lcg_last)


	quit()
	modulus = -1
	for mod_value in reversed(range(30000, 2**16)):
		try:
			a = solve_a(lcg_0, lcg_1, lcg_2, mod_value)
			c = solve_c(lcg_0, lcg_1, mod_value, a)
			next = lcg(mod_value, a, c, lcg_2)

			if next == lcg_3:
				modulus = mod_value
				break
		except ZeroDivisionError:
			pass

	# Now we have all the parameters


	print(f'Doing guesses:')
	lcg_last = lcg_3
	for x in range(30):
		lcg_last = lcg(mod_value, a, c, lcg_last)
		print(f'>> next {x}: {lcg_last}')
		guess(lcg_last)



if __name__ == '__main__':
	main()