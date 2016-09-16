import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import numba
sns.set()

def ecdf(data):
    return np.sort(data), np.arange(1, len(data)+1) / len(data)

# Backtracking
def backtrack_steps():
    x = 0
    steps = 0
    # Limits the distance the polymerase can backtrack to 2000,
    # ~ the average mRNA length in yeast.
    while -2000 < x < 1:
        if np.random.random() < 0.5:
            x += 1
            steps += 1
        else:
            x -= 1
            steps += 1
    return steps


def testSpeed(numberOfRuns=10000):
    backtracks = []
    for i in range(0, numberOfRuns):
        backtracks.append(backtrack_steps())


backtracks = testSpeed()
x, y = ecdf(backtracks)
# Plot the CCDF
plt.loglog(x, 1 - y, '.')

# Plot the asymptotic power law
t_smooth = np.logspace(0.5, 8, 100)
plt.loglog(t_smooth, 1 / np.sqrt(t_smooth))

# Label axes
plt.xlabel('time (s)')
plt.ylabel('CCDF')

"""
# Plotting
x, y = ecdf(backtracks)
plt.plot(x, y, marker='.', linestyle='none', markersize='10',
        color='blue', alpha = 0.1)
plt.xscale('log')
plt.yscale('log')
plt.margins(0.02)
plt.ylabel('ECDF')
plt.xlabel('Number of steps')
plt.show()"""
