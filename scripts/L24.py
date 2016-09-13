import numpy as np
import scipy.special
import scipy.stats
#import bootcamp_utils
import matplotlib.pyplot as plt
import seaborn as sns
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

xa_high = np.loadtxt('../data/xa_high_food.csv')
xa_low = np.loadtxt('../data/xa_low_food.csv')

def ecdf(data):
    '''Compute x,y values for an empirical distribution
    function.'''
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)
    #y = np.arange(1/len(x), 1+(1/len(x)), 1/len(x))

    return x, y

x_high, y_high = ecdf(xa_high)
x_low, y_low = ecdf(xa_low)

plt.plot(x_high, y_high, marker='.',
        linestyle='none', markersize=20, alpha = 0.5)
plt.plot(x_low, y_low, marker='.',
        linestyle='none', markersize=20, alpha = 0.5)
plt.xlabel('Cross section areal $\mu ^2$')
plt.ylabel('ECDF')
plt.title('ECDF of Egg Cross Sectional Area')
plt.legend(('High ECDF', 'Low ECDF'), loc='lower right')
plt.margins(0.02, 0.02)
plt.show()
