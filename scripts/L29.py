# Import modules
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Specify parameters.
n_gen = 16

# Chance of having a beneficial mutation
r = 1e-5

# total number of cells
n_cells = 2**(n_gen-1)

ai_samples = np.random.binomial(n_cells, r, size=100000)
def ecdf(data):
     return np.sort(data), np.arange(1, len(data)+1) / len(data)

# Report mean and standard deviation
print('AI mean', np.mean(ai_samples))
print('AI std', np.std(ai_samples))
print('AI Fano factor', np.var(ai_samples) / np.mean(ai_samples))

def draw_random_mutation(n_gen, r):
    """Draw a sample out of the Luria-Delbruck distribution"""
    # Initialize number of mutants
    n_mut = 0

    for g in range(n_gen):
        n_mut = 2 * n_mut + np.random.binomial(2**g - 2 * n_mut, r)

    return n_mut

def sample_random_mutation(n_gen, r, size=1):
    samples = np.empty(size)

    for i in range(size):
        samples[i] = draw_random_mutation(n_gen, r)

    return samples

rm_samples = sample_random_mutation(n_gen, r, size=100000)

rm_samples = np.sort(rm_samples)
y = np.arange(1, len(rm_samples)+1 / len(rm_samples)

plt.semilogx(rm_samples, y, '.', markersize=10)

print('RM mean', np.mean(rm_samples))
print('RM std', np.std(rm_samples))
print('RM Fano factor', np.var(rm_samples) / np.mean(rm_samples))
