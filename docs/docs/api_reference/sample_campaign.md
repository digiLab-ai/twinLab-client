---
sidebar_position: 6
---

# Sample campaign

Sample an existing campaign.

## Arguments

| Name       | Type   | Description               |
| ---------- | ------ | ------------------------- |
| `eval`     | string | Path to evaluation inputs |
| `campaign` | string | Campaign label            |

**NOTE:** Evaluation data must be a CSV file.

## Example

```python
import twinlab_client as tl

file = "resources/data/eval.csv"
campaign = "my_campaign"
df_mean, df_std = tl.sample_campaign(file, campaign)
```
