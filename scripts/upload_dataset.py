# Standard imports
import os

# Project imports
import twinlab as tl

print()  #  Initial white space
directory = "datasets"
filename = "biscuits.csv"
filepath = os.path.join(directory, filename)
tl.upload_dataset(filepath, verbose=True, debug=True)
