import numpy as np

def PeriodCal(a):
    """
    Calculate the orbital period using Kepler's Third Law
    
    Parameters:
    semi_major_axis (float): SMA

    Returns:
    float: Orbital period in years
    """
    return np.sqrt(a ** 3)