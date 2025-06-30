import itertools

def squibble_index(c):
    return (ord(c) * 3 + 7) % 13

def gizmo_xor(a, b):
    return (a ^ b) ^ ((a & b) << 1)

def decrypt_flag(enc_flag_hex, key):
    junk_pool = b"QWERTYUIOPASDFGHJKLZXCVBNM9876543210"
    flag = ""
    j = 0

    for i in range(0, len(enc_flag_hex), 2):
        byte_hex = enc_flag_hex[i:i+2]
        enc_byte = int(byte_hex, 16)

        input_char = key[j % len(key)]
        junk_char = junk_pool[j % len(junk_pool)]
        mix = squibble_index(input_char) ^ gizmo_xor(junk_char, ord(input_char))

        flag_char = chr(enc_byte ^ mix)
        flag += flag_char
        j += 1

    return flag

def brute_force(enc_flag_hex, charset, length):
    for combo in itertools.product(charset, repeat=length):
        key = 'LMF40' #key is LMF40
        flag = decrypt_flag(enc_flag_hex, key)
        if flag.startswith("BMCTF{"):
            print(f"[+] Key found: {key}")
            print(f"[+] Flag: {flag}")
            return
    print("[-] No valid key found.")

# Replace this with the actual hex string from your binary
obfuscated_flag_hex = "ded9c1150affdeb62317c8a9e72226a5e6df3372dac1e14e0b"

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
brute_force(obfuscated_flag_hex, charset, length=5)