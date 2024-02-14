import hashlib

x = b'SCHOFIELD'

y = hashlib.sha256(x).hexdigest()

4, 5, 3, 6, 2, 7, 1, 8

z = y[4] + y[5] + y[3] + y[6] + y[2] + y[7] + y[1] + y[8]

print(z)

zz = 'e584b363'