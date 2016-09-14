import numpy as np
import scipy.special
import scipy.stats
import bootcamp_utils
import matplotlib.pyplot as plt
import seaborn as sns

rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Specify parameters
alpha = 1
beta = 0.2
delta = 0.3
gamma = 0.8
dt = 0.01
t = np.arange(0, 60, dt)


# Make an array to store the number of bacteria
r = np.empty_like(t)
f = np.empty_like(t)

# Set the initial number of bacteria
r[0] = 10
f[0] = 1

for i in range(1, len(t)):
    r[i] = r[i-1] + (r[i-1] * dt * alpha) - (dt * beta * f[i-1] * r[i-1])
    f[i] = f[i-1] + (f[i-1] * dt * delta * r[i-1]) - (dt * gamma * f[i-1])

plt.plot(t, r)
plt.plot(t, f)
plt.margins(0.02)
plt.xlabel('Time')
plt.ylabel('Count')
plt.legend(('Rabbits', 'Foxes'), loc='upper left')
