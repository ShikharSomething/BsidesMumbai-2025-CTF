import numpy as np
import base64
from sympy import Matrix

# Load cipher and fake key
with open("cipher.txt", "r") as f:
    cipher_b64 = f.read().strip()

cipher_bytes = base64.b64decode(cipher_b64)
cipher_blocks = np.frombuffer(cipher_bytes, dtype=np.uint8)

# Load fake key and rotate it back
fake_key = np.load("fake_key.npy")
real_key = np.rot90(fake_key, -1)  # rotate clockwise to undo the fake

# Compute modular inverse of the real key using sympy
mod = 256
sym_key = Matrix(real_key.tolist())
inv_key = np.array(sym_key.inv_mod(mod)).astype(np.int64)

# Decrypt cipher blocks
block_size = 4
decrypted = []

for i in range(0, len(cipher_blocks), block_size):
    block = np.array(cipher_blocks[i:i+block_size])
    dec_block = inv_key @ block % mod
    decrypted.extend(dec_block)

# Convert to ASCII string, remove padding
plaintext = ''.join(chr(b) for b in decrypted).rstrip('\x00')
print(plaintext)

#flag: BMCTF{Matrixie_crypt10n}