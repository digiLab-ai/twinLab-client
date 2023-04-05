import numpy as np
import pandas as pd

# Parameters
seed = 123
n = 100
infile = 'datasets/ukaea.csv'
outfile = 'datasets/ukaea_small.csv'

# Set random seed
np.random.seed(seed)

# Read in full data
df = pd.read_csv(infile)

# Subsample and save
df_small = df.sample(n, replace=False)
df_small.to_csv(outfile, index=False)
