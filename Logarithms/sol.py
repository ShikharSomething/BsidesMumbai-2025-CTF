from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

# Encrypted chunks (example — replace with actual)
parts = [
    base64.b64decode("rSwvpNKUcK4="),  # from /tmp/f0
    base64.b64decode("ncxAvF750uA="),  # from /tmp/f1
    base64.b64decode("E17U6kCBm7Y="),  # etc.
    base64.b64decode("Sqf4h8/bxLc="),
]
ciphertext = b''.join(parts)

# AES key (from /tmp/key)
key = base64.b64decode("jXvXBfB+1Ts1uaQCNQ/iww==")

# Decrypt
cipher = AES.new(key, AES.MODE_ECB)
plaintext = unpad(cipher.decrypt(ciphertext), 16)
print(plaintext.decode())
