---
sidebar_position: 7
---

# Delete datasets

Remove a campaign owned by the user.

## Endpoint URL

`https://api.twinlab.ai/twinlab/delete_campaign`

## Headers

| Name         | Type   | Description                  |
| ------------ | ------ | ---------------------------- |
| `X-Group`    | string | Organisation user belongs to |
| `X-User`     | string | Unique user name             |
| `X-Campaign` | string | Unique name of the campaign  |

## Response fields

| Name      | Type   | Description          |
| --------- | ------ | -------------------- |
| `message` | string | Confirmation message |

## Example

### Query

```shell
curl -i -X POST https://api.twinlab.ai/twinlab/delete_campaign \
    -H "X-Group: digilab" \
    -H "X-User: dodders" \
    -H "X-Dataset: my_data.csv" \
```

### Response

```bash
{
    "status": 200,
    "message": "my_data.csv campaign deleted successfully"
}
```
