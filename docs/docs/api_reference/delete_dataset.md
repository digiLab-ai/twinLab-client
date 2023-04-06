---
sidebar_position: 3
---

# Delete datasets

Remove a dataset owned by the user.

## Endpoint URL

`https://api.twinlab.ai/twinlab/delete_dataset`

## Headers

| Name        | Type   | Description                  |
| ----------- | ------ | ---------------------------- |
| `X-Group`   | string | Organisation user belongs to |
| `X-User`    | string | Unique user name             |
| `X-Dataset` | string | Unique name of the dataset   |

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
    -H "X-Dataset: my_data.csv" \
```

### Response

```bash
{
    "status": 200,
    "message": "my_data.csv dataset deleted successfully"
}
```
