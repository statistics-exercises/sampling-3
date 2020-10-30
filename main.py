# Uncomment these two lines if you get an error saying pandas is not available
#from os import system
#system('pip install pandas')
import numpy as np 
import pandas as pd

# This reads in the data from the movie_data.txt file
movies_df = pd.read_csv("movie_data.txt", index_col="Title")

# You need to set the following variables using the information in the data
# frame and the commands that are explained in the panel on the right.
runtime_mean = 
rating_min = 
rating_max = 
votes_median = 
metascore_p25 = 
metascore_p75 = 
