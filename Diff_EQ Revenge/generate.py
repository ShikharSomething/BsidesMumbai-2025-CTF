import math

# Define the flag
flag = "BMCTF{D3r1VIn6_FlAG5_L0L!}"
ascii_vals = [ord(c) for c in flag]

# Split ASCII values
f_vals = ascii_vals[:13]
g_vals = ascii_vals[13:]

# Define evaluation function
def eval_poly(coeffs, x):
    return sum(val * x**i / math.factorial(i) for i, val in enumerate(coeffs))

# Define polynomial printing function
def print_poly(coeffs, name):
    terms = []
    for i, c in enumerate(coeffs):
        coeff = c / math.factorial(i)
        if i == 0:
            terms.append(f"{coeff:.6f}")
        elif i == 1:
            terms.append(f"{coeff:.6f}*x")
        else:
            terms.append(f"{coeff:.6f}*x^{i}")
    poly_str = " + ".join(terms)
    print(f"{name}(x) = {poly_str}\n")

# Choose x values (distinct)
x_values = list(range(1, 14))  # x = 1 to 13

# Evaluate F(x) and G(x)
f_samples = [(x, eval_poly(f_vals, x)) for x in x_values]
g_samples = [(x, eval_poly(g_vals, x)) for x in x_values]

# Print polynomials
print("F(x) polynomial (from first 13 characters):")
print_poly(f_vals, "F")

print("G(x) polynomial (from next 13 characters):")
print_poly(g_vals, "G")

# Print evaluations
print("F(x) samples:")
for x, fx in f_samples:
    print(f"F({x}) = {fx:.6f}")

print("\nG(x) samples:")
for x, gx in g_samples:
    print(f"G({x}) = {gx:.6f}")
