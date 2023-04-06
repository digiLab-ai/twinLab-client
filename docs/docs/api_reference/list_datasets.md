---
sidebar_position: 2
---

# List datasets

List all datasets owned by the user.

## Endpoint URL

`https://api.twinlab.ai/twinlab/list_datasets`

## Headers

| Name      | Type   | Description                  |
| --------- | ------ | ---------------------------- |
| `X-Group` | string | Organisation user belongs to |
| `X-User`  | string | Unique user name             |

## Response fields

| Name      | Type         | Description               |
| --------- | ------------ | ------------------------- |
| `message` | list[string] | List of dataset filenames |

## Example

### Query

```shell
curl -i -X GET https://api.twinlab.ai/twinlab/list_datasets \
    -H "X-Group: digilab" \
    -H "X-User: dodders" \
```

### Response

```bash
{
    "status": 200,
    "message": "Datasets: my_data.csv, my_data2.csv"
}
```
