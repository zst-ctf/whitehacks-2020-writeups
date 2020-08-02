# BabyLFSR
Crypto

## Challenge 

DESCRIPTION
My 256 bit key is unbreakable.

Note: The flag's text is an intellegible message. For extra verification, the string 101 should appear in the flag.

Author: prokarius


ATTACHED FILES
encryptCensored.py
out.out


## Solution

### Analyse the source code

Basically we see that there are 4 LFSRs.

where a = bottom 64-bits of seed, b = 2nd 64-bits, c = 3rd 64-bits, d = top 64-bits of seed.


    # Unbruteforcable 256 bit key muahahaha
    seed = random.randrange(2**sum(KEYS))

    # Seeding
    a = LSFR(seed % 2**KEYS[0], TAPS[0], KEYS[0]); seed //= 2**KEYS[0]
    b = LSFR(seed % 2**KEYS[1], TAPS[1], KEYS[1]); seed //= 2**KEYS[1]
    c = LSFR(seed % 2**KEYS[2], TAPS[2], KEYS[2]); seed //= 2**KEYS[2]
    d = LSFR(seed % 2**KEYS[3], TAPS[3], KEYS[3]); seed //= 2**KEYS[3]

If we simplify, we can actually separate out the 256-bit seed into 4 seeds. Also note that the taps and bit length are equal.

    # Unbruteforcable 256 bit key muahahaha
    seed = random.randrange(2**sum(KEYS))

    # Seeding
    a = LSFR(seed0, 15564440312192434176,  64);
    b = LSFR(seed1, 15564440312192434176,  64);
    c = LSFR(seed2, 15564440312192434176,  64);
    d = LSFR(seed3, 15564440312192434176,  64);

Now, realise that we take each bit of the flag, and XOR with the LSFR function.

    def encrypt(self, string):
        bits = []
        key = []
        for char in string:
            out = self.func(list(map(lambda x: x.getNext(), self.lsfr)))
            bits.append(char ^ out)
            key.append(out)
        // more

Also note that the LFSR function is the XOR of all 4 LSFR

	lambda l:l[0]^l[1]^l[2]^l[3]

Since it is 4 LFSR is XOR'ed together anyway, together with the same taps and bit number length. So actually, we can just treat it like one simple shift register.


### Attack method

We take it that our simple shift register is 64-bits long. We have the encrypted output and a censored flag. We can extract the LSFR bits for at least the first 7 characters `WH2020{` using XOR.

And to form a complete LFSR state of 64-bits, we need to extract out 64-bits or 8 characters. So, the issue now is we need to bruteforce the last char. For each bruteforce attempt, we take the 8 characters and XOR encrypted output to get the LFSR state.

So we have many possible flags, and I just looked through the list to see which one is the most coherent.

Bruteforce then I find out the flag at index 83.

	83 b'WH2020{Same_Key_Length_XOR_LFSR_Is_Not_Proper_LFSR_101}'

## Flag

	WH2020{Same_Key_Length_XOR_LFSR_Is_Not_Proper_LFSR_101}
