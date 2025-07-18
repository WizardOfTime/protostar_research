import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

# 设置图形样式
plt.style.use('seaborn-v0_8-poster')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 14

# 创建模拟数据 - 注意现在距离坐标是反向的
x = np.linspace(1.2e14, 0, 500)  # 从右向左排列，模拟原图的坐标方向

# 物质温度 (红色实线)
T_matter = np.zeros_like(x)
T_matter[x > 8e13] = 717  # 右侧区域对应postshock
T_matter[(x <= 8e13) & (x > 4e13)] = 792  # 中间区域对应shock
T_matter[x <= 4e13] = 125  # 左侧区域对应preshock

# 添加过渡区域使曲线更平滑
transition_width = 0.5e13
for i in range(len(x)):
    if 8e13 >= x[i] > 8e13 - transition_width:
        T_matter[i] = 717 + (792 - 717) * (8e13 - x[i]) / transition_width
    elif 4e13 >= x[i] > 4e13 - transition_width:
        T_matter[i] = 792 - (792 - 125) * (4e13 - x[i]) / transition_width

# 辐射温度 (绿色虚线)
T_rad = np.zeros_like(x)
T_rad[x > 8e13] = 717
T_rad[(x <= 8e13) & (x > 4e13)] = 782
T_rad[x <= 4e13] = 111

# 添加过渡区域
for i in range(len(x)):
    if 8e13 >= x[i] > 8e13 - transition_width:
        T_rad[i] = 717 + (782 - 717) * (8e13 - x[i]) / transition_width
    elif 4e13 >= x[i] > 4e13 - transition_width:
        T_rad[i] = 782 - (782 - 111) * (4e13 - x[i]) / transition_width

# 创建图形
fig, ax = plt.subplots(figsize=(12, 8))

# 绘制温度曲线 (注意x轴已经反向)
ax.plot(x / 1e14, T_matter, color='red', linewidth=3, label='Matter Temperature')
ax.plot(x / 1e14, T_rad, color='green', linestyle='--', linewidth=3, label='Radiation Temperature')

# 添加区域分隔线
ax.axvline(0.8, color='gray', linestyle=':', linewidth=1.5, alpha=0.7)
ax.axvline(0.4, color='gray', linestyle=':', linewidth=1.5, alpha=0.7)

# 添加理论值参考线
for T in [125, 717, 792, 111, 782]:
    ax.axhline(T, color='gray', linestyle=':', linewidth=1.5, alpha=0.7)

# 添加区域标注
ax.text(0.2, 800, 'Postshock Region', ha='center', va='center', fontsize=14,
        bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
ax.text(0.6, 800, 'Shock Region', ha='center', va='center', fontsize=14,
        bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
ax.text(1.0, 800, 'Preshock Region', ha='center', va='center', fontsize=14,
        bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

# 添加理论值标注
ax.text(1.0, 140, r'$T_{\mathrm{analytic}} = 111$ K', ha='center', va='bottom', fontsize=12)
ax.text(1.0, 100, r'$T_{\mathrm{sim}} = 125$ K', ha='center', va='top', fontsize=12, color='red')

ax.text(0.6, 820, r'$T_{\mathrm{analytic}} = 782$ K', ha='center', va='bottom', fontsize=12)
ax.text(0.6, 750, r'$T_{\mathrm{sim}} = 792$ K', ha='center', va='top', fontsize=12, color='red')

ax.text(0.2, 740, r'$T_{\mathrm{analytic}} = T_{\mathrm{sim}} = 717$ K',
        ha='center', va='bottom', fontsize=12)

# 设置坐标轴 (保持x轴从左到右增大)
ax.set_xlim(1.2, 0)  # 反向x轴
ax.set_ylim(0, 850)
ax.set_xlabel('Distance ($10^{14}$ cm) → Flow Direction', fontsize=16)
ax.set_ylabel('Temperature (K)', fontsize=16)
ax.set_title('Temperature Profile of a 1D Subcritical Radiating Shock\n'
             r'Gas Velocity $v = 6$ km s$^{-1}$ at Time $t = 5.8 \times 10^4$ s',
             fontsize=18, pad=20)

# 添加小刻度和网格
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.grid(True, which='major', linestyle='-', linewidth=0.5, alpha=0.5)
ax.grid(True, which='minor', linestyle=':', linewidth=0.5, alpha=0.3)

# 添加图例
ax.legend(loc='lower left', framealpha=1, fontsize=14)

plt.tight_layout()
plt.show()
