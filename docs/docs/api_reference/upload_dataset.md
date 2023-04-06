---
sidebar_position: 1
---

# Upload dataset

Upload a CSV file to create a new dataset.

## Arguments

| Name   | Type   | Description  |
| ------ | ------ | ------------ |
| `file` | string | Path to file |

**NOTE:** Data must be a CSV file.

## Example

```python
import twinlab_client as tl

data_file = "resources/data/my_data.csv"
tl.upload_dataset(data_file)
```
