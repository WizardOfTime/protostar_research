import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

gamma = 5/3
mu = 0.5
kB = 1.3806e-16
mH = 1.6726e-24
a_rad = 7.5657e-15
c = 2.9979e10

v_shock = 6e5          # 6 km/s
T_preshock = 20        # K
rho_preshock = 1e-18   # g/cm^3

def kappa(T):
    """Temperature dependent opacity (cm^2/g)"""
    T = np.atleast_1d(T)
    kappa_val = np.zeros_like(T)
    mask = T < 150
    kappa_val[mask] = 0.1 * (T[mask] / 100.0) ** 2
    mask = T >= 150
    kappa_val[mask] = 0.1 * np.exp(-(T[mask] - 150.0) / 50.0)
    return kappa_val if len(kappa_val) > 1 else kappa_val.item()

# Rankine-Hugoniot
def shock_jump(gamma, Mach, rho1, T1):
    rho2 = rho1 * (gamma + 1) * Mach**2 / ((gamma - 1) * Mach**2 + 2)
    T2 = T1 * (2 * gamma * Mach**2 - (gamma - 1)) * ((gamma - 1) * Mach**2 + 2) / ((gamma + 1)**2 * Mach**2)
    return rho2, T2

cs_preshock = np.sqrt(gamma * kB * T_preshock / (mu * mH))
Mach = v_shock / cs_preshock
rho_postshock, T_postshock = shock_jump(gamma, Mach, rho_preshock, T_preshock)

def radiative_loss(T, rho):
    return 4 * a_rad * c * kappa(T) * rho * (T**4 - T_preshock**4)

# ODE
def shock_odes(x, y):
    rho, v, T, Erad = y
    kappa_T = kappa(T)

    mass_flux = rho_preshock * v_shock
    dvdx = 0.0

    P = rho * kB * T / (mu * mH)
    dPdx = - radiative_loss(T, rho) / max(v, 1e-20)

    dTdx = dPdx * (mu * mH) / (rho * kB)

    dEraddx = -3.0 * kappa_T * rho * Erad / c

    drhodx = - (rho / v) * dvdx  # 如果v恒定则drho/dx=0

    return [drhodx, dvdx, dTdx, dEraddx]

y0 = [
    rho_postshock,
    v_shock * rho_preshock / rho_postshock,
    T_postshock,
    a_rad * T_postshock**4
]

x_span = [0.1e14, 1.2e14]
sol = solve_ivp(shock_odes, x_span, y0, method='BDF',
                dense_output=True, rtol=1e-6, atol=1e-8)

x_plot = np.linspace(0.1e14, 1.2e14, 500)
sol_plot = sol.sol(x_plot)
T_matter = sol_plot[2]
T_rad = (sol_plot[3] / a_rad) ** 0.25

plt.figure(figsize=(12, 8))
plt.plot(x_plot / 1e14, T_matter, 'r-', lw=3, label='Matter Temp (sim)')
plt.plot(x_plot / 1e14, T_rad, 'g--', lw=3, label='Radiation Temp (sim)')
plt.axhline(111, color='k', linestyle=':', alpha=0.5, label='Analytic Preshock')
plt.axhline(717, color='b', linestyle=':', alpha=0.5, label='Analytic Postshock')
plt.axhline(792, color='m', linestyle=':', alpha=0.5, label='Shock Peak')
plt.xlabel('Distance (10$^{14}$ cm)')
plt.ylabel('Temperature (K)')
plt.title('1D Radiating Shock Structure\n(Example ODE System)', fontsize=16)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
