# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(match_code):
    match = ipl_matches_array[ipl_matches_array[:,0] == match_code]
    #runs = match[:,16]
    ind = match[:,11]
    runs = pd.Series(match[:,16],index = ind)

    return runs



