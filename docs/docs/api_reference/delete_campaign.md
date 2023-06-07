---
sidebar_position: 8
---

# Delete campaign

Delete campaign from the `twinLab` cloud.

**NOTE:** Your user information is automatically added to the request using the `.env` file.

## Arguments
- `campaign_name`: `str`; name of trained model to delete from the cloud
- `server`: `str`; {`"local"`, `"dev"`, `"stage"`, `"cloud"`}
- `verbose`: `bool`
- `debug`: `bool`

## Example

```python
import twinlab as tl

campaign = "my_campaign"
tl.delete_campaign(campaign)
```
