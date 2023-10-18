from pwn import *

r = remote("http://mercury.picoctf.net:45028/")

# SEND HEAD REQUEST TO ENDPOINT/index.php