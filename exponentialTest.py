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

def exponential_growth(startingArea, r, t):
    return startingArea**(r*t)

timesToPlot = []
areasToPlot = []
for i in range(0, 50):
    timesToPlot.append(i)
    y = exponential_growth(1300, 0.03, i)
    areasToPlot.append(y)

plt.semilogy(timesToPlot, areasToPlot)
