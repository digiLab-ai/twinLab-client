---
sidebar_position: 4
---

# Train campaign

Train a new emulator.

**NOTE:** Your user information is automatically added to the request using the `.env` file.

## Arguments

| Name       | Type   | Description            |
| ---------- | ------ | ---------------------- |
| `params`   | dict   | Emulator configuration |
| `campaign` | string | Campaign label         |

**NOTE:** Data must be a CSV file.

## Example

```python
import json
import twinlab_client as tl

params_file = "resources/data/my_params.json"
with open(params_file, "r") as f:
    params = json.load(f)
campaign = "my_campaign"
tl.train_campaign(params, campaign)
```
