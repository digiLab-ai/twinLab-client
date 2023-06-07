---
sidebar_position: 1
---

# Upload dataset

Upload a dataset to the `twinLab` cloud so that it can be queried and used for training.

**NOTE:** Your user information is automatically added to the request using the `.env` file.

## Arguments

- `filepath_or_df`: `str` | `Dataframe`; location of csv dataset on local machine or `pandas` dataframe
- `dataset_name`: `str`; name for the dataset when saved to the twinLab cloud
- `server`: `str`; {`"local"`, `"dev"`, `"stage"`, `"cloud"`}
- `verbose`: `bool`
- `debug`: `bool`

**NOTE:** Local data must be a CSV file. If a `pandas` dataframe is uploaded then a `dataset_name` must be provided. If a local file is uploaded then the filename with the directories removed will be the uploaded file name, unless a value of `dataset_name` is provided, which will be used preferentially.

## Examples

Upload a local file:
```python
import twinlab as tl

data_filepath = "resources/data/my_data.csv"
tl.upload_dataset(data_filepath) # This will be my_data.csv in the cloud
```

Upload a `pandas` dataframe:
```python
import pandas as pd
import twinlab as tl

dataframe = pd.DataFrame({'X': [1, 2, 3, 4], 'y': [1, 4, 9, 16]})
dataset_name = "test.csv" # Give the dataset a name in the cloud
tl.upload_dataset(dataframe, dataset_name)
```
