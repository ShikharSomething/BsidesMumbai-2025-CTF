def generate_seed():
    seed = 0
    for x in range(100, 0, -1):
        seed += (x * x) ^ (x << 3)
    seed = (seed * 0xDEADBEEF) % 0x7FFFFFFF
    return seed

def encrypt_flag(flag):
    seed = generate_seed()
    encrypted = []
    for c in flag:
        seed = (seed * 1103515245 + 12345) & 0x7fffffff
        encrypted.append(ord(c) ^ ((seed >> 24) & 0xFF))  # match C logic
    return bytes(encrypted)

if __name__ == "__main__":
    flag = "BMCTF{G0tt4_C4tcH_3m_4lL!!}"
    encrypted = encrypt_flag(flag)

    print("// Add this to your C code:")
    print(f"const unsigned char encrypted_flag[] = {{ {', '.join(f'0x{b:02x}' for b in encrypted)} }};")
    print(f"const int flag_length = {len(encrypted)};")
