# twinLab Client

<p align="center">
    <img src="./resources/icons/logo.svg" width="200" height="200" />
</p>

![digiLab](./resources/badges/digilab.svg)
[![slack](https://img.shields.io/badge/slack-@digilabglobal-purple.svg?logo=slack)](https://digilabglobal.slack.com)

Headless interface to the `twinLab` library.

## Installation

```shell
poetry install
```

## Environment setup

```shell
cp .env.example .env
```

and fill in your group and user names.

## Commands

Local or cloud testing:

```python
poetry run python scripts/trigger.py local_or_cloud
```

where the `local_or_cloud` flag is either `local` or `cloud` and where `trigger.py` can be replaced with any of the scripts in the `script` directory.
You need to have a local server for the `twinlab-cloud` repository running for local testing.

## Example

```shell
# Import libraries
import twinlab as tl
import pandas as pd

# Create a dataframe and upload to twinLab cloud
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
df_mean, df_std = tl.sample_campaign(df, campaign='test')
```

## Notebooks

Check out the `notebooks` directory for some examples to get started!

## Documentation

See the live documentation at https://digilab-ai.github.io/twinLab-client/

Or build a copy locally:
```shell
cd docs
yarn start
```
