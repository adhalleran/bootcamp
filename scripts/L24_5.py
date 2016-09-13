import numpy as np
import scipy.special
import scipy.stats
import bootcamp_utils
import matplotlib.pyplot as plt
import seaborn as sns

xa_high = np.loadtxt('../data/xa_high_food.csv')
xa_low = np.loadtxt('../data/xa_low_food.csv')

x_high, y_high = bootcamp_utils.ecdf(xa_high)
x_low, y_low = bootcamp_utils.ecdf(xa_low)

x = np.linspace(1600, 2500, 400)
cdf_high = scipy.stats.norm.cdf(x, loc=np.mean(xa_high), scale = np.std(xa_high))
cdf_low = scipy.stats.norm.cdf(x, loc=np.mean(xa_low), scale = np.std(xa_low))

plt.plot(x_high, y_high, marker='.',
        linestyle='none', markersize=20, alpha = 0.5)
plt.plot(x_low, y_low, marker='.',
        linestyle='none', markersize=20, alpha = 0.5)

plt.plot(x, cdf_high, color='gray')
plt.plot(x, cdf_low, color='gray')
plt.xlabel('Cross section areal $\mu ^2$')
plt.ylabel('ECDF')
plt.title('ECDF of Egg Cross Sectional Area')
plt.legend(('High ECDF', 'Low ECDF'), loc='lower right')
plt.margins(0.02, 0.02)
plt.show()
