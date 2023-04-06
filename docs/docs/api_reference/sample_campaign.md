---
sidebar_position: 6
---

# Sample campaign

Sample an existing campaign.

## Endpoint URL

`https://api.twinlab.ai/twinlab/sample_campaign`

## Headers

| Name         | Type   | Description                  |
| ------------ | ------ | ---------------------------- |
| `X-Group`    | string | Organisation user belongs to |
| `X-User`     | string | Unique user name             |
| `X-Campaign` | string | Unique name of the campaign  |

## Form data

Data must be a CSV file.

## Response fields

| Name      | Type   | Description                  |
| --------- | ------ | ---------------------------- |
| `message` | string | Confirmation message         |
| `y_mean`  | JSON   | Predicted mean values        |
| `y_std`   | JSON   | Predicted standard deviation |

## Example

### Query

```shell
curl -i -X POST https://api.twinlab.ai/twinlab/sample_campaign \
    -H "X-Group: digilab" \
    -H "X-User: dodders" \
    -H "X-Campaign: my_campaign" \
    -F "data=@resources/data/my_eval.csv;type=text/csv"
```

### Response

```bash
{
    "status": 200,
    "message": "Sampling complete",
    "y_mean": "[1.02, 2.12, 3.43, 2.34]",
    "y_std": "[0.13, 0.14, 0.09, 0.07]",
}
```
