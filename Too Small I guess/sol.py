from Crypto.Util.number import *
from Crypto.Util.number import long_to_bytes

# Given values
e = 65537
m = bytes_to_long(b"BMCTF{S1z3_Matt3r5}")

# Step 1: Factor N (very small primes)
p = getPrime(128)
q = getPrime(128)
N = p*q
# Step 2: Compute phi(N)
phi = (q - 1) * (p - 1)

# Step 3: Compute private key d
d = pow(e, -1, phi)
print(N)
print(p)
print(q)

# Step 4: Decrypt
c = 38646786673711502908673828610162116832942524955056840750113041881419282482585
x = (pow(m, e, N))
print("Encrypted message:", x)
