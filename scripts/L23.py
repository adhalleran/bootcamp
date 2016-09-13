import numpy as np
import scipy.special
import scipy.stats
#import bootcamp_utils
import matplotlib.pyplot as plt
import seaborn as sns
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

data_txt = np.loadtxt('../Data/collins_switch.csv', delimiter = ',', skiprows = 2)

# Slice out iptg and gfp
iptg = data_txt[:,0]
gfp = data_txt[:,1]
sem = data_txt[:,2]

# # Plot iptg vs. gfp
# plt.semilogx(iptg, gfp, linestyle ='none', marker='.', markersize=20)
# plt.title('IPTG Titration')
# plt.xlabel('IPTG concentration (mM)')
# plt.ylabel('GFP concentration (au)')
# plt.ylim(-0.02, 1.02)
# plt.xlim(8e-4, 15)

# plt.errorbar(iptg, gfp, yerr=sem, linestyle='none',
#              marker='.', markersize=20)
# plt.title('IPTG Titration')
# plt.xlabel('IPTG concentration (mM)')
# plt.ylabel('GFP concentration (au)')
# plt.ylim(-0.02, 1.02)
# plt.xlim(8e-4, 15)
# plt.xscale('log')

# Plotting exercise 3
plt.errorbar(iptg, gfp, yerr=sem, linestyle='none',
             marker='.', markersize=20)
plt.title('IPTG Titration')
plt.xlabel('IPTG concentration (mM)')
plt.ylabel('GFP concentration (au)')
plt.ylim(-0.02, 1.02)
plt.xlim(8e-4, 15)
plt.xscale('log')
