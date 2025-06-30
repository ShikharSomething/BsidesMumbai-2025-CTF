import sys

def xor_crypt(data_bytes, key_bytes):
    """
    Performs XOR encryption/decryption on a byte sequence.
    This function mirrors the xor_crypt logic in the C challenge.

    Args:
        data_bytes (bytes): The data to be encrypted/decrypted.
        key_bytes (bytes): The key to use for XORing.

    Returns:
        bytes: The result of the XOR operation.
    """
    result = bytearray(len(data_bytes))
    key_len = len(key_bytes)
    for i in range(len(data_bytes)):
        result[i] = data_bytes[i] ^ key_bytes[i % key_len]
    return bytes(result)

def solve_challenge():
    """
    Solves the C reverse engineering challenge by decrypting the expected key.
    """
    # These bytes directly correspond to `correct_key_encrypted` in the C code
    correct_key_encrypted_hex = "1f0a1c0c1b110a1a150a1c0c1b110a1a1500"
    correct_key_encrypted_bytes = bytes.fromhex(correct_key_encrypted_hex)

    # This key directly corresponds to `encryption_key` in the C code
    encryption_key_bytes = b"RE!" # 'b' prefix denotes a byte string

    # Decrypt the expected key
    decrypted_key_bytes = xor_crypt(correct_key_encrypted_bytes, encryption_key_bytes)

    # The decrypted key is the expected input
    expected_input = decrypted_key_bytes.decode('ascii') # Assuming ASCII for the key string

    # The flag is hardcoded in the C program after correct key input
    flag = "flag{X0R_Is_Fun}"

    print(f"To solve the challenge, you need to enter the following secret key:")
    print(f"Secret Key: {expected_input}")
    print(f"\nAfter entering this key, the program will reveal the flag:")
    print(f"Flag: {flag}")

if __name__ == "__main__":
    solve_challenge()
