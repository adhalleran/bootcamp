import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import skimage.io
import skimage.exposure
import skimage.morphology
import skimage.filters


sns.set()
phase_im = skimage.io.imread('data/bsub_100x_phase.tif')
cfp_im = skimage.io.imread('data/bsub_100x_CFP.tif')

# plt.imshow(phase_im, cmap=plt.cm.viridis)

# Plot the histogram of the phase image
hist_phase, bins_phase = skimage.exposure.histogram(phase_im)

plt.plot(bins_phase, hist_phase)
plt.xlabel('pixel value')
plt.ylabel('count')

# Apply our threshold
thresh = 260
im_phase_thresh = phase_im < thresh

plt.close()

with sns.axes_style('dark'):
    plt.imshow(im_phase_thresh, cmap=plt.cm.Greys_r)

with sns.axes_style('dark'):
    plt.imshow(cfp_im, cmap=plt.cm.viridis)

# Slice out region with a hot pixel.
plt.close()
with sns.axes_style('dark'):
    plt.imshow(cfp_im[150:250, 450:550]/cfp_im.max(), cmap=plt.cm.viridis)

# Generate a structural element
selem = skimage.morphology.square(100)
cfp_filt = skimage.filters.median(cfp_im, selem)

plt.close()
with sns.axes_style('dark'):
    plt.imshow(cfp_filt, cmap=plt.cm.viridis)
