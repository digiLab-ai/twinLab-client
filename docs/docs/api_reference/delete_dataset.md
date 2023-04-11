---
sidebar_position: 3
---

# Delete dataset

Remove a dataset owned by the user.

**NOTE:** Your user information is automatically added to the request using the `.env` file.

## Example

```python
import twinlab_client as tl

dataset = "my_dataset.csv"
tl.delete_dataset(dataset)
```
