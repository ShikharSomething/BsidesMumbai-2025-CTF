from sympy import symbols, interpolate, diff, simplify
from sympy.abc import x

# F(x) samples (first 13 chars)
f_samples = [
    (1, 194.549218), (2, 553.628249), (3, 1575.859045),
    (4, 4411.968220), (5, 12075.765546), (6, 32453.576104),
    (7, 85960.808002), (8, 224003.476522), (9, 570836.394390),
    (10, 1412774.210144), (11, 3377556.365402), (12, 7776330.180779),
    (13, 17225433.502382)
]

# G(x) samples (next 13 chars)
g_samples = [
    (1, 205.394500), (2, 597.964949), (3, 1614.528082),
    (4, 4243.548403), (5, 11121.686466), (6, 29227.103377),
    (7, 76604.974278), (8, 198477.260841), (9, 503905.264969),
    (10, 1244691.416493), (11, 2976002.219867), (12, 6866688.882078),
    (13, 15270867.949549)
]

# Function to recover ASCII values
def recover_ascii(samples):
    poly = interpolate(samples, x)
    poly = simplify(poly)

    ascii_vals = []
    for i in range(13):
        deriv = diff(poly, x, i)
        val = deriv.subs(x, 0)
        ascii_vals.append(round(val))
    return ascii_vals

# Recover both halves of the flag
ascii_f = recover_ascii(f_samples)
ascii_g = recover_ascii(g_samples)

# Print ASCII values and flag
print("ASCII F:", ascii_f, "→", ''.join(chr(c) for c in ascii_f))
print("ASCII G:", ascii_g, "→", ''.join(chr(c) for c in ascii_g))

flag = ''.join(chr(c) for c in ascii_f + ascii_g)
print("\n✅ Recovered Flag:", flag)
