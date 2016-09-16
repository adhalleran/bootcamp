import numpy as np
import skimage.filters
import skimage.io
import skimage.morphology
import skimage.exposure
import matplotlib.pyplot as plt
import seaborn as sns
import os
import scipy
sns.set()

areas = []
for image in os.listdir('../data/bacterial_growth'):
    if '.tif' in image:
        imageToProcess = '../data/bacterial_growth/' + image
        print(imageToProcess)
        threshold = 600
        mCherry = skimage.io.imread(imageToProcess)
        mCherry_thresh = mCherry > threshold
        mCherry_area = mCherry_thresh.sum()
        areas.append(mCherry_area)
    else:
        pass

# Convert to an array
areas = np.array(areas)

# Convert time to hours and create an array
t = np.arange(len(areas)) * 0.25

def growth(t, log_b_0, log_tau):
    """Growth function using exponentials."""
    return np.exp(log_b_0) * np.exp(t / np.exp(log_tau))

logP, _ = scipy.optimize.curve_fit(growth, t, areas, p0=None)

print(*tuple(np.exp(logP)))
print('R (square microns) = ', np.exp(logP)[0])
print('T (hours)= ', np.exp(logP)[1])

# Get smooth values
t_smooth = np.linspace(0, t.max(), 100)
y_smooth = growth(t_smooth, *tuple(logP))

# Make smooth plot and plot data
plt.plot(t_smooth, y_smooth, marker='None', linestyle='-', color='gray')
plt.plot(t, areas, marker='.', linestyle='', markersize=10)
plt.xlabel('Time (hours)')
plt.ylabel('Area (pixels$^2$)')
plt.title('Exponential growth')
