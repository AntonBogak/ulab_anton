import numpy as np
velocities = [] # empty velocity list for once they're all cleaned up
def meters_to_c(vel_list):
    '''
    Converts velocities from meters per second to decimal of c. If they are already a decimal of c, do nothing.
    '''
    c = 299792458
    for i in vel_list:
        if i <= 1:
            velocities.append(i) #Does nothing to the value if it's already a decimal
        else:
            velocities.append(i / c) #Changes the value to a decimal of c
    return velocities

def lorentz_factor(velocities):
    '''
    Calculates the Lorentz factor (gamma) for each velocity in the list.
    INPUT: velocities (list of decimal values representing fractions of the speed of light)
    OUTPUT: List of Lorentz factors for each velocity
    '''
    gamma_factors = []
    for velocity in velocities:
        if velocity >= 1:
            gamma_factors.append("Undefined (v >= c)")  # Lorentz factor is undefined for v >= c
        else:
            gamma = 1 / np.sqrt(1 - velocity**2)
            gamma_factors.append(gamma)
    return gamma_factors
    
def stillframe_dilation(velocities, time):
    '''
    This calculates the difference in time between a stationary observer and an observer moving at a speed as a fraction of C
    INPUT: velocities (input as a an array of decimal values of the speed of light)
    INPUT: time (the proper time that passes) (in seconds)
    RESULT: Time difference between the observers
    '''
    timediffs = []
    gamma_factors = lorentz_factor(velocities)
    for gamma in gamma_factors:
        if gamma == "Undefined (v >= c)":
            timediffs.append("Objects with mass can't travel faster than or at the speed of light.")
        else:
            timeprime = time * gamma  # Time experienced by the moving observer
            timediff = timeprime - time  # Time difference between observers
            timediffs.append(timediff)
    
    return np.array(timediffs, dtype=object)


