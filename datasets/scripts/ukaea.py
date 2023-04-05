import numpy as np
import pandas as pd

# Parameters
seed = 123
n_small = 100
infile = "datasets/ukaea.csv"
outfile_small = "datasets/ukaea_small.csv"
n_test = 5
outfile_test = "campaigns/ukaea/test.csv"

# Set random seed
np.random.seed(seed)

# Read in full data
df = pd.read_csv(infile)

# Subsample and save smaller dataframe
df_small = df.sample(n_small, replace=False)
df_small.to_csv(outfile_small, index=False)

# Test dataframe
df_test = df[-n_test:]
df_test.to_csv(outfile_test, index=False)
