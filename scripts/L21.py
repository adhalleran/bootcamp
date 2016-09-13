import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

xa_high = np.loadtxt('../data/xa_high_food.csv')
xa_low = np.loadtxt('../data/xa_low_food.csv')

low_min = np.min(xa_low)
low_max = np.max(xa_low)
high_min = np.min(xa_high)
high_max = np.max(xa_high)
global_min = np.min([low_min, high_min])
global_max = np.min([low_max, high_max])

bins = np.arange(global_min-50, global_max+50, 50)

_ = plt.hist(xa_low, normed=True, bins=bins, histtype='stepfilled', alpha=0.5)
_ = plt.hist(xa_high, normed=True, bins=bins, histtype='stepfilled', alpha=0.5)
plt.xlabel('Cross-sectional area (um$^2$)')
plt.ylabel('Frequency')
plt.legend(('Low concentration', 'high concentration'), loc='upper right')

plt.show()
# Save the figure
plt.savefig('Histogram.pdf', bbox_inches='tight')
