from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

E_l = -70  # mV, resting potential
V_T = -55  # mV, threshold voltage
tau_m = 10  # ms, membrane time constant
R_mI_e_values = [12, 16]  # mV, different values of R_m * I_e
t = np.linspace(0, 100, 1000)  # time from 0 to 100 ms

def diff_eq(V, t, R_mI_e, E_l, tau_m):
    return (E_l - V + R_mI_e) / tau_m



# Adjusting the integrate-and-fire model solution with starting V = E_l and restricted V-axis

def solve_integrate_and_fire_adjusted(R_mI_e, E_l, V_T, tau_m, t):
    V = np.full_like(t, E_l)  # Initialize with V = E_l
    spikes = []
    for i in range(1, len(t)):
        # Euler method to solve the differential equation
        V[i] = V[i-1] + diff_eq(V[i-1], t[i-1], R_mI_e, E_l, tau_m) * (t[i] - t[i-1])
        # Check if voltage reaches threshold
        if V[i] >= V_T:
            V[i] = E_l  # Reset to E_l
            spikes.append(t[i])  # Record spike time
    return V, spikes

# Re-plotting with adjustments
plt.figure(figsize=(6, 4))

# Solve and plot for each R_mI_e value
for R_mI_e in R_mI_e_values:
    V, spikes = solve_integrate_and_fire_adjusted(R_mI_e, E_l, V_T, tau_m, t)
    plt.plot(t, V, label=f'R_mI_e={R_mI_e} mV')
    if spikes:  # Only plot spikes if they exist
        plt.scatter(spikes, [V_T]*len(spikes), color='red', marker='*')

plt.xlabel('t (ms)')
plt.ylabel('V (mV)')
plt.ylim(-75, -45)  # Restricting V-axis
plt.legend()
plt.tight_layout()
plt.savefig('integrate_and_fire.png')  # Saving the figure
plt.show()

