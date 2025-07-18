import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

plt.style.use('seaborn-v0_8-poster')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 14


x = np.linspace(1.2e14, 0, 500)

T_matter = np.zeros_like(x)
T_matter[x > 8e13] = 717  
T_matter[(x <= 8e13) & (x > 4e13)] = 792 
T_matter[x <= 4e13] = 125 

transition_width = 0.5e13
for i in range(len(x)):
    if 8e13 >= x[i] > 8e13 - transition_width:
        T_matter[i] = 717 + (792 - 717) * (8e13 - x[i]) / transition_width
    elif 4e13 >= x[i] > 4e13 - transition_width:
        T_matter[i] = 792 - (792 - 125) * (4e13 - x[i]) / transition_width

T_rad = np.zeros_like(x)
T_rad[x > 8e13] = 717
T_rad[(x <= 8e13) & (x > 4e13)] = 782
T_rad[x <= 4e13] = 111

for i in range(len(x)):
    if 8e13 >= x[i] > 8e13 - transition_width:
        T_rad[i] = 717 + (782 - 717) * (8e13 - x[i]) / transition_width
    elif 4e13 >= x[i] > 4e13 - transition_width:
        T_rad[i] = 782 - (782 - 111) * (4e13 - x[i]) / transition_width

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(x / 1e14, T_matter, color='red', linewidth=3, label='Matter Temperature')
ax.plot(x / 1e14, T_rad, color='green', linestyle='--', linewidth=3, label='Radiation Temperature')

ax.axvline(0.8, color='gray', linestyle=':', linewidth=1.5, alpha=0.7)
ax.axvline(0.4, color='gray', linestyle=':', linewidth=1.5, alpha=0.7)

for T in [125, 717, 792, 111, 782]:
    ax.axhline(T, color='gray', linestyle=':', linewidth=1.5, alpha=0.7)

ax.text(0.2, 800, 'Postshock Region', ha='center', va='center', fontsize=14,
        bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
ax.text(0.6, 800, 'Shock Region', ha='center', va='center', fontsize=14,
        bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
ax.text(1.0, 800, 'Preshock Region', ha='center', va='center', fontsize=14,
        bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

ax.text(1.0, 140, r'$T_{\mathrm{analytic}} = 111$ K', ha='center', va='bottom', fontsize=12)
ax.text(1.0, 100, r'$T_{\mathrm{sim}} = 125$ K', ha='center', va='top', fontsize=12, color='red')

ax.text(0.6, 820, r'$T_{\mathrm{analytic}} = 782$ K', ha='center', va='bottom', fontsize=12)
ax.text(0.6, 750, r'$T_{\mathrm{sim}} = 792$ K', ha='center', va='top', fontsize=12, color='red')

ax.text(0.2, 740, r'$T_{\mathrm{analytic}} = T_{\mathrm{sim}} = 717$ K',
        ha='center', va='bottom', fontsize=12)

ax.set_xlim(1.2, 0)  # 反向x轴
ax.set_ylim(0, 850)
ax.set_xlabel('Distance ($10^{14}$ cm) → Flow Direction', fontsize=16)
ax.set_ylabel('Temperature (K)', fontsize=16)
ax.set_title('Temperature Profile of a 1D Subcritical Radiating Shock\n'
             r'Gas Velocity $v = 6$ km s$^{-1}$ at Time $t = 5.8 \times 10^4$ s',
             fontsize=18, pad=20)

ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.grid(True, which='major', linestyle='-', linewidth=0.5, alpha=0.5)
ax.grid(True, which='minor', linestyle=':', linewidth=0.5, alpha=0.3)
ax.legend(loc='lower left', framealpha=1, fontsize=14)

plt.tight_layout()
plt.show()
