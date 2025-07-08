# boot.py

# if supervisor is_usb_connected_
#   # we're connected to the USB so we want to code
#   storage.mount readOnly = True 
# else:
#   # we're not connected to the USB so we want to run the program and save the data to storage
#   storage.mount readOnly = False


# code.py
# 0. imports
from ulab import numpy as np
from micropython import const

# 1.  initialize variables, iterations, tag ID, numpy array of measurements


# UWB Constants
TAG_ID = const(1) # This should be different for each tag

# Algorithm Constants
NUM_ITERARIONS = const(100) # Number of iterations to try different timing settings
NUM_CANDIDATES = const(100) # Number of candidates to generate for each iterations
NUM_MEASUREMENTS = const(1000) # Number of measurements of range to take when evaluating the candidate

EDM_actual = np.ndarray([
    [0,1,2,3,4,5,6], #0
    [0,1,2,3,4,5,6], #1
    [0,1,2,3,4,5,6], #2
    [0,1,2,3,4,5,6], #3
    [0,1,2,3,4,5,6], #4
    [0,1,2,3,4,5,6], #5
    [0,1,2,3,4,5,6], #6
])

EDM_measured = EDM_actual.copy()

# 1.1 have an easy place to update the E_actual matrix of nxn distances from each unit
#   that has been measured with a laser distance sensor

# 1.1.1 Save the default antenna delay measurements to see how much we improved

# 1.2 Set antenna delay to ZERO

# 2. loop through iterations

# 3. follow the rest of the algorithm




# helper methods

# getDelayEstimateCandidates:

# evaludateCandidates:

# getCurrentEDMMeasured: