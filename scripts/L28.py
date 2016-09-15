import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def ecdf(data):
    return np.sort(data), np.arange(1, len(data)+1) / len(data)

def draw_bs_reps(data, func, number=1):
    """ Use to generate boot strapped data that draws the same number
    of samples as the length of your data vector and computes a user-defined
    input function. Defaults to generate one boostrap."""
    bs_replicates = np.empty(number)
    for i in range(number):
        bs_sample = np.random.choice(data, size=len(data), replace=True)
        bs_replicates[i] = func(bs_sample)

    return bs_replicates


bd_1975 = np.loadtxt('../data/beak_depth_scandens_1975.csv')

x_1975, y_1975 = ecdf(bd_1975)
plt.plot(x_1975, y_1975, marker='.', linestyle='none', markersize='10',
        color='blue', label='1975')


plt.xlabel('Beak depth (mm)')
plt.ylabel('ECDF')
plt.legend(loc= 'lower right')
#plt.show()
