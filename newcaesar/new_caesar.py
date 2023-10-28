import string

# 73 % 16 = 10 (i)

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16] # 16 characters

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		print(LOWERCASE_OFFSET)
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag = "ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieihihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih"
key = "a"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
	#					 always 0 since len(key) == 1
	enc += shift(c, key[i % len(key)])
print(enc)

"""
REVERSE
"""

# import string
# enc ="mlnklfnknljflfmhjimkmhjhmljhjomhmmjkjpmmjmjkjpjojgjmjpjojojnjojmmkmlmijimhjmmj"
# ALPHABET = string.ascii_lowercase[:16] 

# b16 = []

# for i in range(len(ALPHABET)):
# 	b16.append("")

# for i in enc:
# 	for k in range(len(ALPHABET)):
# 		index = ALPHABET.index(i)
# 		if(k <= index):
# 			b16[k]+=chr(index -k+97)
# 		else:
# 			b16[k]+=chr(index +16-k+97)

# for k in range(len(ALPHABET)):
#     flag=""
# 	b = b16[k]
# 	for i in range(0, len(b), 2):
# 		if(b[i+1] in ALPHABET and b[i] in ALPHABET):
# 			index1 = ALPHABET.index(b[i])
# 			index2 = ALPHABET.index(b[i+1])
# 			flag+= chr((index1 <<4) +index2)
# 	print(flag)
