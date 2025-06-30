import base64
import random
from datetime import datetime
from faker import Faker
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import codecs

fake = Faker()
log_lines = []

# === Setup AES Encryption ===
FLAG = b'BMCTF{1_Kn0w_Ab0uT_A35_4ND_L0g5!!}'
KEY = get_random_bytes(16)
cipher = AES.new(KEY, AES.MODE_ECB)
encrypted_flag = cipher.encrypt(pad(FLAG, 16))
chunks = [encrypted_flag[i:i+8] for i in range(0, len(encrypted_flag), 8)]

# === Helper Functions ===
def apache_time():
    return datetime.utcnow().strftime("%d/%b/%Y:%H:%M:%S +0000")

def random_ip():
    return fake.ipv4()

def make_log(ip, req, ua):
    return f'{ip} - - [{apache_time()}] "GET {req} HTTP/1.1" 200 123 "-" "{ua}"'

def rot13_payload(php_code):
    encoded = codecs.encode(php_code, 'rot_13')
    return f'<?php eval(str_rot13("{encoded}")); ?>'

# === Normal Log Noise ===
for _ in range(20000):  # Increased for realism
    ip = random_ip()
    req = fake.uri_path()
    ua = fake.user_agent()
    log_lines.append(make_log(ip, req, ua))

# === Poisoned Entries (AES chunks) ===
for i, chunk in enumerate(chunks):
    b64_chunk = base64.b64encode(chunk).decode()
    raw_php = f"file_put_contents('/tmp/f{i}', base64_decode('{b64_chunk}'));"
    ua_payload = rot13_payload(raw_php)
    log_lines.append(make_log("133.7.133.7", "/index.php?page=../../logs/access.log", ua_payload))

# === AES Key Writer ===
b64_key = base64.b64encode(KEY).decode()
raw_php = f"file_put_contents('/tmp/key', base64_decode('{b64_key}'));"
ua_payload = rot13_payload(raw_php)
log_lines.append(make_log("133.7.133.7", "/index.php?page=../../logs/access.log", ua_payload))

# === Final Execution Payload ===
final_php = """
$key = file_get_contents('/tmp/key');
$data = '';
for ($i = 0; $i < 6; $i++) {
  $data .= file_get_contents('/tmp/f'.$i);
}
$dec = openssl_decrypt($data, 'aes-128-ecb', $key, OPENSSL_RAW_DATA);
echo 'FLAG: '.$dec;
""".strip().replace("\n", "")

ua_payload = rot13_payload(final_php)
log_lines.append(make_log("133.7.133.7", "/index.php?page=../../logs/access.log", ua_payload))

# === Final Shuffle to Disperse Malicious Requests ===
random.shuffle(log_lines)

# === Write to file ===
with open("access.log", "w") as f:
    for line in log_lines:
        f.write(line + "\n")

print("[+] Obfuscated access.log generated with dispersed malicious payloads.")
