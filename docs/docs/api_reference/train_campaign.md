---
sidebar_position: 4
---

# Train campaign

Train a new emulator.

## Endpoint URL

`https://api.twinlab.ai/twinlab/train_campaign`

## Headers

| Name         | Type   | Description                  |
| ------------ | ------ | ---------------------------- |
| `X-Group`    | string | Organisation user belongs to |
| `X-User`     | string | Unique user name             |
| `X-Campaign` | string | Unique name of the campaign  |

## Parameters data

Parameters must be a JSON file.

## Response fields

| Name      | Type   | Description          |
| --------- | ------ | -------------------- |
| `message` | string | Confirmation message |

## Example

### Query

```shell
curl -i -X POST https://api.twinlab.ai/twinlab/delete_dataset \
    -H "X-Group: digilab" \
    -H "X-User: dodders" \
    -H "X-Campaign: my_campaign" \
    -d @resources/data/my_params.json
```

### Response

```bash
{
    "status": 200,
    "message": "Training complete"
}
```
