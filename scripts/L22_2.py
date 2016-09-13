import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns

# Load in data set
data = np.loadtxt('../data/retina_spikes.csv', skiprows=2, delimiter=',')

# Slice out time and voltage
t = data[:,0]
V = data[:,1]
plt.plot(t, V)
#plt.xlabel('t')
#plt.ylabel('V')

plt.xlim(1395, 1400)
plt.show()
