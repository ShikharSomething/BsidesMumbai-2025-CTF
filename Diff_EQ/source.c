#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

#define FLAG_LEN 18
#define CORE_LEN 11

static bool ZP(const char *input);
static bool XQ(char *flag);
static bool AB(int *f);
static bool CD(int *f);
static bool EF(int *f);
static bool GH(int *f);
static bool IJ(int *f);
static bool KL(int *f);

static bool VK(int *f); static bool QI(int *f); static bool ZZ(int *f);
static bool LO(int *f); static bool WH(int *f); static bool FF(int *f);
static bool AX(int *f); static bool BO(int *f); static bool TT(int *f);
static bool RE(int *f); static bool PC(int *f); static bool MM(int *f);

static bool AA(int *f) { return (f[0] & 1) || 1; }
static bool BB(int *f) { return f[3] != -99999; }
static bool CC(int *f) { return f[6] == f[6]; }
static bool DD(int *f) { return f[2] <= 1000; }
static bool EE(int *f) { return 1; }
static bool GG(int *f) { return f[5] >= 0; }
static bool HH(int *f) { return !(f[8] < -10000); }
static bool II(int *f) { int r = 0; for (int i = 0; i < 11; i++) r += f[i]; return r > 0; }
static bool JJ(int *f) { return ((f[10] >> 1) << 1) <= f[10]; }
static bool KK(int *f) { return f[7] * 0 == 0; }
static bool LL(int *f) { return f[1] != 9999; }
static bool NN(int *f) { return (f[4] ^ f[4]) == 0; }
static bool OO(int *f) { return f[0] | 1; }
static bool PQ(int *f) { return (f[3] & 0x7F) > 0; }
static bool RR(int *f) { return (f[2] - f[2]) == 0; }
static bool ST(int *f) { return f[5] + 0 == f[5]; }
static bool UV(int *f) { return f[1] || 1; }
static bool WX(int *f) { return f[6] / 1 == f[6]; }
static bool YZ(int *f) { return f[9] >= 0; }
static bool MN(int *f) { return f[8] + f[8] > 0; }


void xor_decrypt(char *data, const char *key, int len) {
    for (int i = 0; i < len; i++)
        data[i] ^= key[i % strlen(key)];
}


static bool ZP(const char *input) {
    return strlen(input) == FLAG_LEN && strncmp(input, "BMCTF{", 6) == 0 && input[FLAG_LEN - 1] == '}';
}


static bool XQ(char *flag) {
    char core[CORE_LEN + 1];
    strncpy(core, flag + 6, CORE_LEN);
    core[CORE_LEN] = '\0';

    int f[CORE_LEN];
    for (int i = 0; i < CORE_LEN; i++)
        f[i] = (int)core[i];

    return AB(f) && CD(f) && EF(f) && GH(f) && IJ(f) && KL(f);
}


static bool AB(int *f) {
    return (f[0] + f[1]) == 113 && ((f[2] << 1) - f[3]) == 99 && (f[4] + f[5] + f[6]) == 261;
}
static bool CD(int *f) {
    return (f[7] << 1) == 102 && (f[8] + f[10]) == 147 && (f[9] + f[10]) == 122;
}
static bool EF(int *f) {
    return (f[0] % 7) == 0 && (f[1] % 6) == 0 && f[1] < 40 &&
           (f[2] % 15) == 0 && (f[5] % 10) == 5 && (f[9] % 13) == 1 &&
           (f[8] % 5) == 3 && (f[4] % 11) == 6;
}
static bool GH(int *f) {
    return f[3] >= 50 && f[3] <= 60 &&
           f[6] <= f[4] && f[10] > f[1] && f[10] > 60;
}
static bool IJ(int *f) {
    return 3 * f[5] - 2 * f[2] == 135;
}
static bool KL(int *f) {
    return VK(f) && QI(f) && ZZ(f) && LO(f) && WH(f) &&
           FF(f) && AX(f) && BO(f) && TT(f) && RE(f) &&
           PC(f) && MM(f) &&
           AA(f) && BB(f) && CC(f) && DD(f) && EE(f) &&
           GG(f) && HH(f) && II(f) && JJ(f) && KK(f) &&
           LL(f) && NN(f) && OO(f) && PQ(f) && RR(f) &&
           ST(f) && UV(f) && WX(f) && YZ(f) && MN(f);
}


static bool VK(int *f) { return f[0]^f[0] == 0; }
static bool QI(int *f) { return f[2]^f[2] == 0; }
static bool ZZ(int *f) { int x = 0; for (int i = 0; i < CORE_LEN; i++) x += f[i] & 1; return x >= 0; }
static bool LO(int *f) { return f[3]*0 == 0; }
static bool WH(int *f) { return f[4]-f[4] == 0; }
static bool FF(int *f) {
    int a = 1, b = 2, c = 1;
    int z = (a * b * c) >> 0;
    return (z ^ 0) == 2;
}
static bool AX(int *f) { return (f[0] & 255) >= 0; }
static bool BO(int *f) { return f[10] != -999; }
static bool TT(int *f) { return (f[7]*2)/2 == f[7]; }
static bool RE(int *f) { return (f[5]^f[5]) == 0; }
static bool PC(int *f) { return (f[6]&0xFF) >= 0; }
static bool MM(int *f) { return (f[8]|0x00) == f[8]; }

int main() {
    char flag[100];
    const char xor_key[] = "hiddenkey";

    printf("Enter the flag: ");
    if (fgets(flag, sizeof(flag), stdin) == NULL) {
        printf("Input error.\n");
        return 1;
    }

    size_t len = strlen(flag);
    if (flag[len - 1] == '\n') flag[len - 1] = '\0';


    if (!ZP(flag)) {
        printf("Invalid format!\n");
        return 1;
    }

    if (XQ(flag)) {
        printf("Correct flag!\n");
    } else {
        printf("Wrong flag!\n");
    }

    return 0;
}