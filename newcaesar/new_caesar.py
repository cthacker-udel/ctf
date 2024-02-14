import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
print('alphabet = ', ALPHABET)

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

def unshift(c, k):
	t1 = ord(c) + LOWERCASE_OFFSET
	t2 = ord(k) + LOWERCASE_OFFSET
	return ALPHABET[(t1 - t2) % len(ALPHABET)]

encoded_key = 'ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih'
print(len(encoded_key))

flag = "a"
key = "p"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

b16 = b16_encode(flag) # twice the len of the original flag
enc = ""


for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])
print(enc)
