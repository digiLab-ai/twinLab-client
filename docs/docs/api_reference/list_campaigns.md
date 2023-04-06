---
sidebar_position: 5
---

# List campaigns

List the trained emulators.

## Endpoint URL

`https://api.twinlab.ai/twinlab/list_campaigns`

## Headers

| Name      | Type   | Description                  |
| --------- | ------ | ---------------------------- |
| `X-Group` | string | Organisation user belongs to |
| `X-User`  | string | Unique user name             |

## Response fields

| Name      | Type   | Description          |
| --------- | ------ | -------------------- |
| `message` | string | Confirmation message |

## Example

### Query

```shell
curl -i -X GET https://api.twinlab.ai/twinlab/list_campaigns \
    -H "X-Group: digilab" \
    -H "X-User: dodders"
```

### Response

```bash
{
    "status": 200,
    "message": "Campaign: my_campaign my_campaign2"
}
```
