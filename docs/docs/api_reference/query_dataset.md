---
sidebar_position: 2
---

# Query dataset

Query a dataset that exists on the `twinLab` cloud by printing summary statistics.

**NOTE:** Your user information is automatically added to the request using the `.env` file.

## Arguments

- `dataset_name`: `str`; name of dataset on S3 (same as the uploaded file name)
- `server`: `str`; {`"local"`, `"dev"`, `"stage"`, `"cloud"`}
- `verbose`: `bool`
- `debug`: `bool`

## Returns

`pandas` dataframe containing summary statistics for the dataset.

## Example

```python
import twinlab as tl

dataset_name = "my_dataset.csv"
df = tl.query_dataset(dataset_name)
print(df)
```
