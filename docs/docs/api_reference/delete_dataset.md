---
sidebar_position: 9
---

# Delete dataset

Delete a dataset from the `twinLab` cloud.

**NOTE:** Your user information is automatically added to the request using the `.env` file.

## Arguments
- `dataset_name`: `str`; name of dataset to delete from the cloud
- `server`: `str`; {`"local"`, `"dev"`, `"stage"`, `"cloud"`}
- `verbose`: `bool`
- `debug`: `bool`

## Example

```python
import twinlab as tl

dataset_name = "my_dataset.csv"
tl.delete_dataset(dataset_name)
```
