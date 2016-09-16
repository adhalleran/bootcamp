import numpy as np
# Our image processing tools
import skimage.filters
import skimage.io
import skimage.morphology
import skimage.exposure
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

mCherry = skimage.io.imread('../data/bacterial_growth/bacillus_042.tif')
# with sns.axes_style('dark'):
#     skimage.io.imshow(mCherry/ mCherry.max())

threshold = 600

mCherry_thresh = mCherry > threshold

mCherry_area = mCherry_thresh.sum()
print(mCherry_area)

# Add a 10um scale bar (155 * pixel width = 10um).
# mCherry_thresh[800:810, 400:410+155] = 1

with sns.axes_style('dark'):
    skimage.io.imshow(mCherry_thresh / mCherry_thresh.max(), cmap=plt.cm.viridis)

# hist_mCherry, bins_mCherry = skimage.exposure.histogram(mCherry)
# plt.fill_between(bins_mCherry, hist_mCherry, alpha = 0.5)
