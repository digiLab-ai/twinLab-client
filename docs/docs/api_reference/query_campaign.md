---
sidebar_position: 5
---

# Query campaign

Get summary statistics for a pre-trained campaign in the `twinLab` cloud.

**NOTE:** Your user information is automatically added to the request using the `.env` file.

## Arguments

- `campaign_name`: `str`; name of trained model to query
- `server`: `str`; {`"local"`, `"dev"`, `"stage"`, `"cloud"`}
- `verbose`: `bool`
- `debug`: `bool`

## Returns

dictionary containing summary statistics for the dataset.

## Example

```python
import twinlab_client as tl

campaign = "my_campaign"
tl.query_campaign(campaign)
```
