---
sidebar_position: 7
---

# Delete datasets

Remove a campaign owned by the user.

**NOTE:** Your user information is automatically added to the request using the `.env` file.

## Arguments

| Name       | Type   | Description    |
| ---------- | ------ | -------------- |
| `campaign` | string | Campaign label |

## Example

```python
import twinlab_client as tl

campaign = "my_campaign"
tl.delete_campaign(campaign)
```
