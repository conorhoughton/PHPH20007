import numpy as np
import matplotlib.pyplot as plt

# Constants
tau = 1.0
t = np.linspace(0, 3, 100)

# Function for exponential relaxation
def h(t, h0, tau):
    return 1 + (h0 - 1) * np.exp(-t / tau)

# Generating curves for different initial conditions
h1 = h(t, 3, tau)
h2 = h(t, 2, tau)
h3 = h(t, 0, tau)

# Plotting
plt.figure(figsize=(4, 2.5))  # Width: 3 inches, Height: 2 inches
plt.plot(t, h1, label='h(0) = 3')
plt.plot(t, h2, label='h(0) = 2')
plt.plot(t, h3, label='h(0) = 0')
plt.axhline(y=1, color='grey', linestyle='--', label='h = 1')

plt.xlabel('t', labelpad=2) 
plt.ylabel('h(t)', labelpad=2)

plt.legend()
plt.xlim(0, 3)
plt.ylim(0, 3)
plt.tight_layout()
plt.savefig('relax.png')  # Save the figure
plt.show()

