def generate_key():
    seed = 0
    for x in range(100, 0, -1):
        seed += (x * x) ^ (x << 3)
    seed = (seed * 0xDEADBEEF) % 0x7FFFFFFF
    return seed

def xor_decrypt(data, key):
    decrypted = bytearray()
    for b in data:
        key = (key * 1103515245 + 12345) & 0x7FFFFFFF
        decrypted.append(b ^ ((key >> 24) & 0xFF))
    return decrypted

enc_flag = bytes([
    0x02, 0x38, 0x5e, 0x6f, 0x2d, 0x16, 0x60, 0x1e, 0x35, 0x65, 0x37, 0x66, 0x10, 0x25, 0x33, 0x76, 0x37, 0x00, 0x4c, 0x4c, 0x5b, 0x61, 0x03, 0x05, 0x5e, 0x7d, 0x0a
])

key = generate_key()
decrypted = xor_decrypt(enc_flag, key)

try:
    print("Flag:", decrypted.decode())
except UnicodeDecodeError:
    print("Flag (raw bytes):", decrypted)
