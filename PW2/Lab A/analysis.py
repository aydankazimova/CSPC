"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration
  - integrate acceleration back up -> recover velocity and position
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid


# --------------------------------------------------
# TODO 1: Read freefall.csv
# --------------------------------------------------

data = np.loadtxt("freefall.csv", delimiter=",", skiprows=1)

t = data[:, 0]
y = data[:, 1]


# --------------------------------------------------
# TODO 2: Differentiate position -> velocity
#         velocity -> acceleration
# --------------------------------------------------

v = np.gradient(y, t)
a = np.gradient(v, t)

print(f"Mean acceleration: {np.mean(a):.3f} m/s^2")
print(f"Acceleration standard deviation: {np.std(a):.3f} m/s^2")


# --------------------------------------------------
# TODO 3 & 4: Integrate acceleration back
# --------------------------------------------------

# Acceleration -> velocity
v_recovered = cumulative_trapezoid(a, t, initial=0) + v[0]

# Velocity -> position
y_recovered = cumulative_trapezoid(v_recovered, t, initial=0) + y[0]


# --------------------------------------------------
# Part 4: Compare recovered position with original
# --------------------------------------------------

difference = np.abs(y_recovered - y)

print(f"Largest position difference: {np.max(difference):.3f} m")


# --------------------------------------------------
# TODO 4: Plot position, velocity, acceleration
# --------------------------------------------------

fig, axes = plt.subplots(3, 1, figsize=(10, 12), sharex=True)


# Position
axes[0].plot(t, y, label="Measured position")
axes[0].plot(t, y_recovered, label="Recovered position")
axes[0].set_ylabel("Position (m)")
axes[0].set_title("Position")
axes[0].legend()
axes[0].grid(True)


# Velocity
axes[1].plot(t, v, label="Velocity")
axes[1].plot(t, v_recovered, label="Recovered velocity")
axes[1].set_ylabel("Velocity (m/s)")
axes[1].set_title("Velocity")
axes[1].legend()
axes[1].grid(True)


# Acceleration
axes[2].plot(t, a, label="Acceleration")
axes[2].axhline(
    -9.81,
    linestyle="--",
    label="True acceleration = -9.81 m/s²"
)
axes[2].set_xlabel("Time (s)")
axes[2].set_ylabel("Acceleration (m/s²)")
axes[2].set_title("Acceleration")
axes[2].legend()
axes[2].grid(True)


plt.tight_layout()

# Save figure
plt.savefig("motion.png", dpi=150)

plt.show()
# --------------------------------------------------
# BONUS: 2D tracked trajectory
# --------------------------------------------------

data2 = np.loadtxt("trajectory.csv", delimiter=",", skiprows=1)

t2 = data2[:, 0]
x = data2[:, 1]
y2 = data2[:, 2]

# Differentiate x and y separately
vx = np.gradient(x, t2)
vy = np.gradient(y2, t2)

# Speed = sqrt(vx^2 + vy^2)
speed = np.sqrt(vx**2 + vy**2)

# Plot the 2D trajectory
plt.figure(figsize=(8, 6))
plt.plot(x, y2)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("2D Tracked Trajectory")
plt.grid(True)
plt.axis("equal")
plt.tight_layout()
plt.savefig("trajectory_path.png", dpi=150)
plt.show()

# Plot speed versus time
plt.figure(figsize=(8, 6))
plt.plot(t2, speed)
plt.xlabel("Time (s)")
plt.ylabel("Speed (m/s)")
plt.title("Speed vs Time")
plt.grid(True)
plt.tight_layout()
plt.savefig("speed.png", dpi=150)
plt.show()