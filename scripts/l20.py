import numpy as np

xa_high = np.loadtxt('../data/xa_high_food.csv')
xa_low = np.loadtxt('data/xa_low_food.csv')

def xa_to_diameter(xa):
    """Convert xa into diameters"""

    diameter = np.swrt(xa * 4 / np.pi)

    return diameter
