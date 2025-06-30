import matplotlib.pyplot as plt

# F(x) samples
f_samples = [
    (1, 194.549218), (2, 553.628249), (3, 1575.859045),
    (4, 4411.968220), (5, 12075.765546), (6, 32453.576104),
    (7, 85960.808002), (8, 224003.476522), (9, 570836.394390),
    (10, 1412774.210144), (11, 3377556.365402), (12, 7776330.180779),
    (13, 17225433.502382)
]

# G(x) samples
g_samples = [
    (1, 205.394500), (2, 597.964949), (3, 1614.528082),
    (4, 4243.548403), (5, 11121.686466), (6, 29227.103377),
    (7, 76604.974278), (8, 198477.260841), (9, 503905.264969),
    (10, 1244691.416493), (11, 2976002.219867), (12, 6866688.882078),
    (13, 15270867.949549)
]

# Extract x and y values
x_f, y_f = zip(*f_samples)
x_g, y_g = zip(*g_samples)

# Plot F(x) with annotations
plt.figure(figsize=(12, 7))
plt.plot(x_f, y_f, marker='o', color='blue', label="F")
for xi, yi in zip(x_f, y_f):
    plt.annotate(f"{yi:.6f}", (xi, yi), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=8, rotation=45)
plt.title("Mystery F")
plt.xlabel("x")
plt.ylabel("F")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("F.png")
plt.close()

# Plot G(x) with annotations
plt.figure(figsize=(12, 7))
plt.plot(x_g, y_g, marker='o', color='green', label="G")
for xi, yi in zip(x_g, y_g):
    plt.annotate(f"{yi:.6f}", (xi, yi), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=8, rotation=45)
plt.title("Mystery G")
plt.xlabel("x")
plt.ylabel("G")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("G.png")
plt.close()
