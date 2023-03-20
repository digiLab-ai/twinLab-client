import digilab as dl
import pandas as pd

# Load data
data = pd.read_csv("resources/data.csv")
samples = pd.read_csv("resources/samples.csv")

# Create emulator
meta = {
    "inputs": ["x0", "x1"],
    "outputs": ["y0", "y1", "y2"],
    "estimator_type": "gaussian_process_regression",
    "train_test_split": 80
}
my_campaign = dl.Campaign(meta)
my_campaign.fit(data)

# Sample
mu, sigma = my_campaign.predict(samples)
