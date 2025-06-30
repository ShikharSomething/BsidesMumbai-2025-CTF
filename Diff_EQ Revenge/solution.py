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

def newton_interpolation(samples):
    n = len(samples)
    x_vals = [pt[0] for pt in samples]
    y_vals = [pt[1] for pt in samples]

    # Create divided difference table
    divided_diff = [y_vals[:]]  # First row is y-values
    for i in range(1, n):
        row = []
        for j in range(n - i):
            numerator = divided_diff[i - 1][j + 1] - divided_diff[i - 1][j]
            denominator = x_vals[j + i] - x_vals[j]
            row.append(numerator / denominator)
        divided_diff.append(row)

    # Construct polynomial using sympy
    from sympy import symbols, simplify
    x = symbols('x')
    polynomial = divided_diff[0][0]
    term = 1
    for i in range(1, n):
        term *= (x - x_vals[i - 1])
        polynomial += divided_diff[i][0] * term

    return simplify(polynomial)

from sympy import symbols, diff, simplify
from sympy.abc import x

# Use the same f_samples and g_samples as in your code

def recover_ascii_custom(samples):
    poly = newton_interpolation(samples)
    ascii_vals = []
    for i in range(13):
        deriv = diff(poly, x, i)
        val = deriv.subs(x, 0)
        ascii_vals.append(round(val))
    return ascii_vals

ascii_f = recover_ascii_custom(f_samples)
ascii_g = recover_ascii_custom(g_samples)

print("ASCII F:", ascii_f, "→", ''.join(chr(c) for c in ascii_f))
print("ASCII G:", ascii_g, "→", ''.join(chr(c) for c in ascii_g))

flag = ''.join(chr(c) for c in ascii_f + ascii_g)
print("\n✅ Recovered Flag:", flag)
