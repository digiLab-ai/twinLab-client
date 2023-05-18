# twinLab Client

<p align="center">
    <img src="./resources/icons/logo.svg" width="200" height="200" />
</p>

![digiLab](./resources/badges/digilab.svg)
[![slack](https://img.shields.io/badge/slack-@digilabglobal-purple.svg?logo=slack)](https://digilabglobal.slack.com)

Headless interface to the `twinLab` library.

## Installation

Most users should use `pip`
```shell
pip install twinlab
```

If you want to modify the client-side code, or have a local installation for some reason
```shell
git clone https://github.com/digiLab-ai/twinLab-client.git
cd twinlab-client
poetry install
```

## Environment setup

You will need a `.env` file in your project directory that looks like the `.env.example` file in this repository
```shell
cp .env.example .env
```
and fill in your twinLab user details.

## Commands

Testing:

```shell
poetry run python scripts/test.py cloud 
```
where `test.py` can be replaced with any of the scripts in the `script` directory.

You need to have a local server for the (private) `twinlab-cloud` repository running for local testing. But local testing can then be run with
```shell
poetry run python scripts/test.py local
```

## Example

Here we create some mock data (which has a quadratic relationship between `X` and `y`) and use `twinLab` to create a surrogate model with quantified uncertainty.
```python
# Import libraries
import twinlab as tl
import pandas as pd

# Create a dataset and upload to twinLab cloud
df = pd.DataFrame({'X': [1, 2, 3, 4], 'y': [1, 4, 9, 16]})
tl.upload_dataset('test.csv', df)

# Train a machine-learning model for the data
params = {
    'filename': 'test.csv',
    'inputs': ['X'],
    'outputs': ['y'],
}
tl.train_campaign(params, campaign='test')

# Evaluate the model on some unseen data
df = pd.DataFrame({'X': [1.5, 2.5, 3.5]})
df_mean, df_std = tl.predict_campaign(df, campaign='test')
```

## Notebooks

Check out the `notebooks` directory for some additional examples to get started!

## Documentation

See the live documentation at https://digilab-ai.github.io/twinLab-client/. Or build a copy locally:
```shell
cd docs
yarn start
```
