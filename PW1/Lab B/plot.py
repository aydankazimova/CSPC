import matplotlib.pyplot as plt
import numpy as np

# TODO 1: Read decay_observed.csv into t and observed arrays
# Skipping header (row 1) and using comma as delimiter
data = np.loadtxt("decay_observed.csv", delimiter=",", skiprows=1)
t = data[:, 0]
observed = data[:, 1]

# TODO 2: Set N0 to the first observed value and build analytical model
LAMBDA = 0.3
N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)

# TODO 3: Make 1x2 subplot with shared x and y axes
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)

# Left: scatter plot of observed data
ax1.scatter(t, observed, color="blue", label="Observed")
ax1.set_title("Observed Data")
ax1.set_xlabel("Time")
ax1.set_ylabel("Count")

# Right: line plot of analytical law
ax2.plot(t, analytical, color="red", label="Analytical")
ax2.set_title("Analytical Model")
ax2.set_xlabel("Time")

# TODO 4: Save figure as figure.png
plt.tight_layout()
plt.savefig("figure.png")