import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d

c = 3e10
a_rad = 7.5657e-15
gamma = 5.0 / 3.0
mu = 0.5
k_B = 1.3807e-16
m_H = 1.6737e-24
R_gas = k_B / (mu * m_H)

v0 = 5e6
T0 = 20
rho0 = 1e-13
E0 = a_rad * T0**4

T_table = np.array([10, 20, 50, 100, 200, 300, 400, 500, 700, 1000, 2000, 4000])
kappa_table = np.array([1e-5, 5e-5, 2e-4, 1e-3, 5e-3, 8e-3, 1e-2, 1.2e-2, 1.5e-2, 2e-2, 3e-2, 4e-2])
opacity_interp = interp1d(T_table, kappa_table, kind='linear', fill_value='extrapolate')

def opacity(T):
    return opacity_interp(T)

def flux_limiter(R):
    return 1.0 / (1.0 + R)

def radiation_hydro_rhs(x, y, dx, rho, v):
    T = y[0]
    Er = y[1]
    E_eq = a_rad * T**4
    kappa = opacity(T)

    dEr_dx = (E_eq - Er) / dx
    R = np.abs(dEr_dx) / (kappa * rho * Er + 1e-30)
    lam = flux_limiter(R)
    F_r = - (c * lam / (kappa * rho)) * dEr_dx
    dF_r_dx = F_r / dx
    G = -dF_r_dx

    dTdx = -G / (rho * R_gas / (gamma - 1))
    dErdx = G
    return [dTdx, dErdx]

def apply_rh_jump(T1, rho1, v1):
    P1 = rho1 * R_gas * T1
    cs1 = np.sqrt(gamma * P1 / rho1)
    M1 = v1 / cs1
    r = ((gamma + 1) * M1**2) / ((gamma - 1) * M1**2 + 2)
    v2 = v1 / r
    rho2 = rho1 * r
    P2 = P1 * (2 * gamma * M1**2 - (gamma - 1)) / (gamma + 1)
    T2 = P2 / (rho2 * R_gas)
    E2 = a_rad * T2**4
    return T2, E2, rho2, v2

def run_region(T_init, E_init, rho, v, x_start, x_end, N):
    x_vals = np.linspace(x_start, x_end, N)
    dx = x_vals[1] - x_vals[0]
    y0 = [T_init, E_init]

    sol = solve_ivp(
        lambda x, y: radiation_hydro_rhs(x, y, dx, rho, v),
        [x_vals[0], x_vals[-1]],
        y0,
        t_eval=x_vals,
        method='RK45',
        rtol=1e-6,
        atol=1e-8
    )
    return sol.t, sol.y

def run_shock_simulation():
    x1, y1 = run_region(T0, E0, rho0, v0, 0.0, 1e15, 1000)
    T1_end = y1[0, -1]
    T2, E2, rho2, v2 = apply_rh_jump(T1_end, rho0, v0)
    x2, y2 = run_region(T2, E2, rho2, v2, x1[-1], x1[-1] + 5e14, 300)
    x_full = np.concatenate([x1, x2])
    T_full = np.concatenate([y1[0], y2[0]])
    Er_full = np.concatenate([y1[1], y2[1]])
    Trad_full = (Er_full / a_rad)**0.25

    plt.figure(figsize=(8, 5))
    plt.plot(x_full / 1e14, T_full, label='Gas Temperature')
    plt.plot(x_full / 1e14, Trad_full, '--', label='Radiation Temperature')
    plt.axhline(111, ls=':', color='gray', label='Pre-shock T')
    plt.axhline(717, ls=':', color='gray', label='Post-shock T')
    plt.xlabel('x (1e14 cm)')
    plt.ylabel('Temperature (K)')
    plt.title('Radiative Shock with Real RH Jump (v0 = 50 km/s, FLD)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    delta_T = Trad_full[:len(x1)] - T_full[:len(x1)]
    T_diff_max = np.max(delta_T)
    T_diff_idx = np.argmax(delta_T)
    x_diff_peak = x1[T_diff_idx] / 1e14

    if T_diff_max > 5:
        print(f"✅ Appearance of preheating zone: T_rad higher than T_gas, maximum difference {T_diff_max:.2f}K, position x ≈ {x_diff_peak:.2f} × 1e14 cm")
    else:
        print("❌ No clear preheating zone was found: T_rad rose almost synchronously with T_gas")

    plt.figure()
    plt.plot(x1 / 1e14, delta_T)
    plt.xlabel('x (1e14 cm)')
    plt.ylabel('T_rad - T_gas (K)')
    plt.title('Pre-shock Temperature Difference')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# === 运行 ===
if __name__ == "__main__":
    run_shock_simulation()
