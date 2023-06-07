---
sidebar_position: 4
---

# Train campaign

Train a campaign in the `twinLab` cloud.

**NOTE:** Your user information is automatically added to the request using the `.env` file.

## Arguments
- `filepath_or_params`: `str` | `dict`; filepath to local json or parameters dictionary for training
- `campaign_name`: `str`; name for the final trained model
- `server`: `str`; {`"local"`, `"dev"`, `"stage"`, `"cloud"`}
- `verbose`: `bool`
- `debug`: `bool`

## Example

Train using a local `json` parameters file:
```python
tl.train_campaign("params.json", "my_campaign", verbose=True)
```

Train via a `python` dictionary:
```python
params = {
    "dataset": "my_dataset",
    "inputs": ["X1", "X2"],
    "outputs": ["y1", "y2"],
}
tl.train_campaign(params, "my_campaign", verbose=True)
```
