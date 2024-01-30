from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# Constants
T = 2 * np.pi  # period of the sine wave
tau_values = [0.25, 2, 4]  # different tau values
t = np.linspace(0, 20, 500)  # time from 0 to 20

# Sine wave function
def y(t):
    return np.sin(t * 2 * np.pi / T)

# Differential equation: tau * dh/dt = y - h
def diff_eq(h, t, tau):
    return (y(t) - h) / tau

# Plotting
plt.figure(figsize=(6, 4))

# Plot the sine wave
plt.plot(t, y(t), label='sine wave', color='black')

# Solve and plot the differential equation for each tau
for tau in tau_values:
    # Initial condition h(0) = 0
    h0 = 0
    # Solve differential equation
    h = odeint(diff_eq, h0, t, args=(tau,))
    # Flatten h to 1D array
    h = h.ravel()
    # Plot the solution
    plt.plot(t, h, label=f'tau={tau}')

plt.xlabel('t')
plt.ylabel('h(t)')
#plt.title()
plt.legend()
plt.tight_layout()
plt.savefig('chasing.png')  # Saving the figure
plt.show()

