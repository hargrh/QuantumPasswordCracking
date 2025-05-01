import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Top 50 real password frequencies from RockYou
frequencies = [
    290729, 79078, 76790, 61958, 51622, 35231, 33989, 32503, 31738, 30104,
    29601, 28413, 27958, 27776, 27243, 27095, 26352, 25561, 24977, 24601,
    24597, 24512, 24052, 23779, 23436, 22963, 22318, 22186, 22012, 21803,
    21701, 21436, 21322, 21153, 21094, 20974, 20869, 20861, 20753, 20575,
    20433, 20388, 20337, 20295, 20287, 20242, 20173, 20054, 20008, 19991
]

# Generate ranks
ranks = np.arange(1, len(frequencies) + 1)

# Apply log to both ranks and frequencies
log_ranks = np.log(ranks)
log_freqs = np.log(frequencies)

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(log_ranks, log_freqs)

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(log_ranks, log_freqs, label="Actual Data", color="blue")
plt.plot(log_ranks, intercept + slope * log_ranks, 'r', label=f"Fit: y = {slope:.2f}x + {intercept:.2f}")
plt.title("Zipf's Law Fit on Top 50 RockYou Passwords")
plt.xlabel("log(Rank)")
plt.ylabel("log(Frequency)")
plt.legend()
plt.grid(True)
plt.show()

# Print R² value
print(f"R² value: {r_value**2:.4f} — {'Good fit!' if r_value**2 > 0.9 else 'Poor fit.'}")