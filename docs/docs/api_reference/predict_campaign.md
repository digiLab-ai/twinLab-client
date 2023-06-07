---
sidebar_position: 7
---

# Predict campaign

Predict from a pre-trained campaign that exists on the `twinLab` cloud.

**NOTE:** Your user information is automatically added to the request using the `.env` file.

## Arguments

- `filepath_or_df`: `str`; location of csv dataset on local machine for evaluation or `pandas` dataframe
- `campaign_name`: `str`; name of pre-trained model to use for predictions
- `server`: `str`; {`"local"`, `"dev"`, `"stage"`, `"cloud"`}
- `verbose`: `bool`
- `debug`: `bool`
  
**NOTE:** Evaluation data must be a CSV file, or a `pandas` dataframe that is interpretable as a CSV.

## Returns
`tuple` containing:
- `df_mean`: `pandas` dataframe containing mean predictions
- `df_std`: `pandas` dataframe containing standard deviation predictions


## Example

Use a local file:
```python
import twinlab_client as tl

filepath = "resources/data/eval.csv" # Local
campaign_name = "my_campaign" # Pre-trained
df_mean, df_std = tl.sample_campaign(file, campaign_name)
```

Use a `pandas` dataframe:
```python
import pandas as pd
import twinlab as tl

df= pd.DataFrame({'X': [1.5, 2.5, 3.5]}
campaign_name = "my_campaign" # Pre-trained
tl.upload_dataset(df, campaign_name)
```
