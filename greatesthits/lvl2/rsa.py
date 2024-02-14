from Crypto.Util.number import *
p=getPrime(1024)
q=getPrime(1024)
n=p*q
e1=32
e2=94
msg=bytes_to_long("REDACTED")
assert(pow(msg,2) < n)
c1 = pow(msg, e1, n)
c2 = pow(msg, e2, n)
print(n)
print(e1)
print(e2)
print(c1)
print(c2)