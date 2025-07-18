import matplotlib.pyplot as plt
import numpy as np

# Distance and temperature data for matter
x_matter = np.array([0.0, 1.0, 1.25, 2.0, 3.5])
T_matter = np.array([700, 700, 800, 0, 0])  # spike to 800 at 1.25

# Distance and temperature data for radiation
x_radiation = np.array([0.0, 1.0, 2.0, 3.0, 3.5])
T_radiation = np.array([700, 600, 400, 100, 0])

plt.figure(figsize=(9, 6))

# Plot matter and radiation
plt.plot(x_matter, T_matter, 'r-', linewidth=2, label='Matter Temperature')
plt.plot(x_radiation, T_radiation, 'g--', linewidth=2, label='Radiation Temperature')

# Add gray reference lines
plt.axhline(782, color='gray', linestyle='--', linewidth=1)
plt.text(3.55, 782, 'Shock 782K', va='center', ha='left', color='gray')

plt.axhline(727, color='gray', linestyle='--', linewidth=1)
plt.text(3.55, 727, 'Post-Shock 727K', va='center', ha='left', color='gray')

plt.axhline(111, color='gray', linestyle='--', linewidth=1)
plt.text(3.55, 111, 'Pre-Shock 111K', va='center', ha='left', color='gray')

# Axis labels and title
plt.xlabel('Distance')
plt.ylabel('Temperature (K)')
plt.title('Temperature Profile with Shock Annotations')

# Legend and grid
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

