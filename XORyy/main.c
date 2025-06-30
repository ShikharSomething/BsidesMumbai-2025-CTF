#include <stdio.h>
#include <string.h>

void xor_crypt(char *data, size_t len, const char *key, size_t key_len) {
    for (size_t i = 0; i < len; i++) {
        data[i] ^= key[i % key_len];
    }
}

int main() {
    char correct_key_encrypted[] = { 0x1f, 0x0a, 0x1c, 0x0c, 0x1b, 0x11, 0x0a, 0x1a, 0x15, 0x0a, 0x1c, 0x0c, 0x1b, 0x11, 0x0a, 0x1a, 0x15, 0x00 }; // Encrypted "ReverseMe!" with key "RE!"
    char encryption_key[] = "RE!";
    char user_input[20];
    size_t correct_key_len = sizeof(correct_key_encrypted) -1;

    printf("Enter the secret key: ");
    if (fgets(user_input, sizeof(user_input), stdin) == NULL) {
        printf("Error reading input.\n");
        return 1;
    }
    user_input[strcspn(user_input, "\n")] = 0;

    char decrypted_correct_key[sizeof(correct_key_encrypted)];
    memcpy(decrypted_correct_key, correct_key_encrypted, sizeof(correct_key_encrypted));
    xor_crypt(decrypted_correct_key, correct_key_len, encryption_key, strlen(encryption_key));


    if (strlen(user_input) == correct_key_len && strcmp(user_input, decrypted_correct_key) == 0) {
        printf("Congratulations! You found the flag: BMCTF{X0R_Is_Fun}\n");
    } else {
        printf("Incorrect key. Try again.\n");
    }

    return 0;
}